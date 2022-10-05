from rest_framework import serializers
from users.models import CustomUser

from .models import Menu, Restaurant, Review


class RestaurantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']


class RestaurantReviewSerializer(serializers.ModelSerializer):
    user = RestaurantUserSerializer(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ['rating', 'restaurant', 'user']


class RestaurantSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    reviews = RestaurantReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(read_only=True)
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Restaurant
        fields = ['name', 'reviews', 'review_count', 'avg_rating', 'location', 'description', 'category', 'cuisine', 'owner']


class ReviewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username']


class ReviewRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'owner']


class ReviewSerializer(serializers.ModelSerializer):
    restaurant = ReviewRestaurantSerializer(read_only=True)
    user = ReviewUserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    user_id = serializers.IntegerField(read_only=True)
    restaurant_id = serializers.IntegerField()
    review = serializers.CharField(allow_blank=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'review', 'rating', 'restaurant', 'reviewer', 'restaurant_id', 'reviewer_id', 'user_id', 'date_visited']


class MenuListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['id', 'file', 'restaurant']
