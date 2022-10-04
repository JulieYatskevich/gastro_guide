from django.urls import path, include
from rest_framework import routers
from .views import RestaurantViewSet, ReviewViewSet, MenuViewSet


router = routers.DefaultRouter(trailing_slash='/?')
router.register(r'restaurants', RestaurantViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'menu', MenuViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
