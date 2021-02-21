from rest_framework import serializers
from .models import AudioBook, Song, PodCast


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['title','duration','created_at','modified_at']


class AudioBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioBook
        fields = ['title','duration','author','narrator']


class PodCastSerializer(serializers.ModelSerializer):

    class Meta:
        model = PodCast
        fields = ['title','duration','host','participants']