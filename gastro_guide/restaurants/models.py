from django.db import models
from enumchoicefield import EnumChoiceField
from users.models import CustomUser

from .enums import CategoryEnum, CuisineEnum


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner')
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True)
    category = EnumChoiceField(CategoryEnum, default=CategoryEnum.CAFE)
    cuisine = EnumChoiceField(CuisineEnum, default=CuisineEnum.OTHER, blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='review')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=Rating.choices, null=False)
    date_visited = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f'{self.reviewer.username} : {self.restaurant.name}'


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to='menus/')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.restaurant.name
