# This script needs to be executed form the django shell, i.e.
# ./python manage.py shell
# >> execfile("./starter/data/load_data_script.py")
import json
from starter.models import Movie

fp = open('starter/data/movies.json', 'r')
data = json.load(fp)
fp.close()

# Start from scratch
Movie.objects.all().delete()

# I'm not going to validate data here for simplicity
for movie_data in data['movies']:
  movie = Movie()
  movie.title = movie_data['title']
  movie.year = int(movie_data['year'])
  movie.mpaa_rating = movie_data['mpaa_rating']
  if movie_data['runtime'] == "":
    runtime_int = 0
  else:
    runtime_int = int(movie_data['runtime'])
  movie.runtime = runtime_int
  movie.ratings = movie_data['ratings']
  movie.synopsis = movie_data['synopsis']
  movie.posters = movie_data['posters']
  movie.abridged_cast = movie_data['abridged_cast']
  movie.release_dates = movie_data['release_dates']
  movie.save()

assert Movie.objects.count() == int(data['total'])
