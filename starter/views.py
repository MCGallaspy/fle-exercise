from django.shortcuts import render
from starter.models import Movie
from itertools import chain
from starter.forms import MovieFilterForm

def landing_page(request):
  filter_form = MovieFilterForm(request.GET)
  if request.method == 'POST':
    search_query = request.POST["search-query"]
    in_title = Movie.objects.filter(title__icontains=search_query)
    in_synopsis = Movie.objects.filter(synopsis__icontains=search_query)
    movies = set(chain(in_title, in_synopsis))
    return render(request, "starter/movie_list.html", {"movies": movies,
                                                       "search_query": search_query,
                                                       "filter_form": filter_form,
                                                      })
  else:
    movies = Movie.objects.all()
    return render(request, "starter/movie_list.html", {"movies": movies,
                                                       "filter_form": filter_form,
                                                      })

def movie_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  return render(request, "starter/movie_detail.html", {"movie": movie})
