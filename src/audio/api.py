from rest_framework import viewsets
from rest_framework.response import Response

from .models import Song, AudioBook, PodCast
from .serializers import (SongSerializer, AudioBookSerializer, PodCastSerializer)


class SongViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet that for listing or retrieving songs.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # serializer_class = SongSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]


class AudioBookViewSet(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer


class PodCastViewSet(viewsets.ModelViewSet):
    queryset = PodCast.objects.all()
    serializer_class = PodCastSerializer