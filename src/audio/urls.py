from django.urls import path, include
from rest_framework import routers

from .api import SongViewSet, AudioBookViewSet, PodCastViewSet

router = routers.DefaultRouter()
router.register('song',SongViewSet)
router.register('audiobook',AudioBookViewSet)
router.register('podcast',PodCastViewSet)


urlpatterns = [
    path('', include(router.urls)),
]