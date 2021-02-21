import datetime
from django.test import TestCase

from ..models import Song, AudioBook, PodCast


class TestModel(TestCase):

    def setUp(self):
        Song.objects.create(title='just a test', duration=1000)
        Song.objects.create(title='New Song', duration=1100)
        AudioBook.objects.create(title='Lion King', duration=4100, author='mama', narrator='jynx')
        PodCast.objects.create(title='Yoga Class', host='django', participants=['hello', 'me'], duration=2500)

    def test_check_field(self):
        song = Song.objects.get(title='New Song')
        audiobook = AudioBook.objects.get(title='Lion King')
        self.assertEqual(song.title, 'New Song')
        self.assertEqual(audiobook.title, 'Lion King')

    def test_check_duration(self):
        song = Song.objects.get(title='New Song')
        self.assertEqual(song.duration, 1100)

    def test_check_count_of_items(self):
        song_objs = Song.objects.count()
        self.assertEquals(song_objs, 2)

    def test_check_meta_label(self):
        audiobook = AudioBook.objects.get(title='Lion King')
        field_label = audiobook._meta.get_field('narrator').verbose_name
        self.assertEqual(field_label, 'narrator name')
        
    def test_check_podcast(self):
        podcast = PodCast.objects.get(host='django')
        self.assertEqual(podcast.title, 'Yoga Class')

    def test_check_len_of_participants_podcast(self):
        podcast = PodCast.objects.get(host='django')
        self.assertLessEqual(len(podcast.participants), 100)