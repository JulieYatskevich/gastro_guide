from django.db.models import Avg, Count
from rest_framework import viewsets

from .models import Menu, Restaurant, Review
from .permissions import (IsAdminOrReadOnly, IsConfirmedOrReadOnly,
                          IsOwnerOrReadOnly)
from .serializers import (MenuListSerializer, RestaurantSerializer,
                          ReviewSerializer)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.annotate(
            review_count=Count('review'),
            avg_rating=Avg('review__rating'),
        )
    serializer_class = RestaurantSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permisssion_class = [IsConfirmedOrReadOnly, ]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuListSerializer
    permission_classes = [IsAdminOrReadOnly]
