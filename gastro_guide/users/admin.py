from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = []

    model = CustomUser

    list_display = ['id', 'username', 'email', 'location', 'gender', 'birth_date']
    list_filter = ['location']
