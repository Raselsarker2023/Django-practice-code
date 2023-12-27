from django.db import models
from Musician.models import MusicianModel


class AlbumModel(models.Model):
    Album_name = models.CharField(max_length=200)
    release_date = models.DateField()
    Rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    musicians = models.ForeignKey(MusicianModel, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.Album_name
