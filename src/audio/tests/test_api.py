import json

from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Song, PodCast, AudioBook
from ..serializers import SongSerializer, PodCastSerializer, AudioBookSerializer


class SongTestCase(APITestCase):

    def test_song_creation(self):
        data = {'title': 'Soup Song', 'duration': 5000}
        response = self.client.post("/song/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_song_delete(self):
        song = Song.objects.create(title='New Song 1', duration=5000)
        response = self.client.delete(f'/song/{song.id}')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_song_update(self):
        data ={'title': 'Playful Poem', 'duration': 1600}
        Song.objects.create(title='New Song 2', duration=5000)
        response = self.client.put("/song/3", data)
        self.assertRedirects(response, '/song/3/', status_code=301, target_status_code=200)


class AudioBookTestCase(APITestCase):

    def test_audiobook_create(self):
        data = {'title': 'Narnia', 'duration': 3000, 'author': 'Jamie', 'narrator':'fox'}
        response = self.client.post("/audiobook/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_audiobook_delete(self):
        audio_book = AudioBook.objects.create(title='Stupid elf', duration=1000, author='kristen', narrator='no_one')
        response = self.client.delete(f"/audiobook/{audio_book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_audiobook_update(self):
        data = {'title': 'Pingu', 'duration': 2000, 'author': 'feny'}
        AudioBook.objects.create(title='mordock', duration=1000, author='lebra', narrator='shawn')
        response = self.client.put("/audiobook/3", data)
        self.assertRedirects(response, '/audiobook/3/', status_code=301, target_status_code=200)


class PodCastTestCase(APITestCase):

    def test_podcast_create(self):
        data = {'title': 'how to get healthy', 'duration': 14000, 'host': 'Beethoven', 'participants': ['a','b','c']}
        response = self.client.post("/podcast/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_podcast_delete(self):
        podcast = PodCast.objects.create(title='Stupid elf', duration=1000, host='kristen',participants=['a','g'])
        response = self.client.delete(f"/podcast/{podcast.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_podcast_update(self):
        data = {'title': 'Hello World', 'duration': 3000, 'host': 'sumpy'}
        PodCast.objects.create(title='dummy', duration=1000, host='sten', participants=['a', 'k'])
        response = self.client.put("/podcast/3", data)
        self.assertRedirects(response, '/podcast/3/', status_code=301, target_status_code=200)