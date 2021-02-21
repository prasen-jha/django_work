from django.db import models
from django.contrib.postgres.fields import ArrayField


class AudioBase(models.Model):
    duration = models.PositiveIntegerField(verbose_name='duration of file in seconds')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Song(AudioBase):
    title = models.CharField( verbose_name='name of the song', null=False, blank=False, max_length=200, unique=True)

    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'

    def get_absolute_url(self):
        return f"song/{self.title}"

    def __str__(self):
        return self.title


class PodCast(AudioBase):
    title = models.CharField(verbose_name='name of the podcast', null=False, blank=False, max_length=200, unique=True)
    host = models.CharField(verbose_name='host_name', max_length=100)
    participants = ArrayField(models.CharField(max_length=100, verbose_name='participant\'s name'),
                              size=10, blank=True, null=True)

    class Meta:
        verbose_name = 'podcast'
        verbose_name_plural = 'podcasts'

    def get_absolute_url(self):
        return f"podcast/{self.title}"

    def __str__(self):
        return self.title


class AudioBook(AudioBase):
    title = models.CharField(verbose_name='name of the title', null=False, blank=False, max_length=200, unique=True)
    author = models.CharField(verbose_name='author name', max_length=100, blank=False, null=False)
    narrator = models.CharField(verbose_name='narrator name', max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'audiobook'
        verbose_name_plural = 'audiobooks'

    def get_absolute_url(self):
        return f"audiobook/{self.title}"

    def __str__(self):
        return self.title
