from django.db import models

class Artist (models.Model):
    name = models.CharField(max_length=1000)

class Genre (models.Model):
    name = models.CharField(max_length=200)

class Song (models.Model):
    name = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre)
    filepath = models.CharField(max_length=1000)
    
    
    
    