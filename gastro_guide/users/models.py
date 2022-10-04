from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField('Дата рождения', default='2000-09-12')
    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
