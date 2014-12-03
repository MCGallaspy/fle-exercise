from django.db import models
from jsonfield import JSONField

class Movie(models.Model):
  title = models.CharField(max_length=200)
  year = models.PositiveIntegerField()
  mpaa_rating = models.CharField(max_length=100)
  runtime = models.PositiveIntegerField()
  ratings = JSONField()
  synopsis = models.TextField()
  posters = JSONField()
  abridged_cast = JSONField()
  release_dates = JSONField()
