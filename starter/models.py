from django.db import models
from jsonfield import JSONField

class CustomFilterQuerySet(models.query.QuerySet):
  def critic_score_filter(self, op, threshold):
    model = models.get_model('starter', 'Movie')
    unfiltered = self
    filtered_pks = []
    for movie in unfiltered:
      if op == "gt" and movie.ratings['critics_score'] >= threshold:
        filtered_pks.append(movie.pk)
      elif op == "lt" and movie.ratings['critics_score'] <= threshold:
        filtered_pks.append(movie.pk)
    return self.filter(pk__in = filtered_pks)

  def audience_score_filter(self, op, threshold):
    model = models.get_model('starter', 'Movie')
    unfiltered = self
    filtered_pks = []
    for movie in unfiltered:
      if op == "gt" and movie.ratings['audience_score'] >= threshold:
        filtered_pks.append(movie.pk)
      elif op == "lt" and movie.ratings['audience_score'] <= threshold:
        filtered_pks.append(movie.pk)
    return self.filter(pk__in = filtered_pks)

  def runtime_filter(self, op, threshold):
    model = models.get_model('starter', 'Movie')
    unfiltered = self
    filtered_pks = []
    for movie in unfiltered:
      if op == "gt" and movie.runtime >= threshold:
        filtered_pks.append(movie.pk)
      elif op == "lt" and movie.runtime <= threshold:
        filtered_pks.append(movie.pk)
    return self.filter(pk__in = filtered_pks)


class CustomFilterManager(models.Manager):
  def get_query_set(self):
    model = models.get_model('starter', 'Movie')
    return CustomFilterQuerySet(model)

    def __getattr__(self, attr, *args):
      try:
        return getattr(self.__class__, attr, *args)
      except AttributeError:
        return getattr(self.get_query_set(), attr, *args)


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

  objects = CustomFilterManager()
