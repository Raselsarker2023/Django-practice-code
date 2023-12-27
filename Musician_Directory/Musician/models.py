from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    id = models.AutoField(primary_key=True)
    Musician_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_no = models.CharField(max_length=15)
    Instrument_Type = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.Musician_Name


