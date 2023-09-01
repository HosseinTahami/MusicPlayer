# Django Imports
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    info = models.TextField(default=True)
    genre_img = models.ImageField()

    def __str__(self) -> str:
        return f"Name: {self.name}"


class Song(models.Model):
    name = models.CharField(max_length=128)
    cover_img = models.ImageField("song_cover_images/")
    description = models.TextField(default=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    audio_file = models.FileField(upload_to="songs/song_files/")
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return f"id: {self.id} || name: {self.name}"
