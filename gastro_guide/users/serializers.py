from django.contrib.auth.models import Group
from .models import CustomUser
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password']

    def save(self, **kwargs):
        user = CustomUser(
            id=self.data.get('id', None),
            username=self.validated_data['username'],
        )

        user.set_password(self.validated_data['password'])
        user.save()
        return user


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def save(self, **kwargs):
        user = CustomUser(username=self.validated_data['username'], email=self.validated_data['email'], birth_date=self.validated_data['birth_date'], gender=self.validated_data['gender'])
        password = self.validated_data['password']

        if len(password) < 6:
            raise serializers.ValidationError('Password length must be greater than 6.')

        user.set_password(password)
        user.save()

        group, _ = Group.objects.get_or_create(name='Посетитель')
        user.groups.add(group)
        user.save()

        return user


class CustomUserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
