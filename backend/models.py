from django.db import models


# Create your models here.
class Leaderboard (models.Model):
    Name = models.CharField(max_length=200)
    Score = models.IntegerField()


class Teams (models.Model):
    Name = models.CharField(max_length=2000)
    Country = models.CharField(max_length=2000)
    Logo = models.CharField(max_length=2000)
    City = models.CharField(max_length=2000)
    StadiumName = models.CharField(max_length=2000)
    StadiumImg = models.CharField(max_length=2000)

