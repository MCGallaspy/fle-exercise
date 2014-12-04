from django.shortcuts import render
from starter.models import Movie

def landing_page(request):
  movies = Movie.objects.all()
  return render(request, "starter/movie_list.html", {"movies": movies})

def movie_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  return render(request, "starter/movie_detail.html", {"movie": movie})
