from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, signup, CustomUserDetailView

router = DefaultRouter()
router.register('all-users', UserViewSet,),

urlpatterns = [
    path('', include(router.urls)),
    path('signup', signup),
    path('profile/<int:pk>', CustomUserDetailView.as_view(), name='profile'),
]
