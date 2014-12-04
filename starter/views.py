from django.shortcuts import render
from starter.models import Movie
from starter.forms import MovieFilterForm
from django.db.models import Q

def landing_page(request):
  filter_form = MovieFilterForm(request.GET)
  context = {}
  movies = []
  context["filter_form"] = filter_form
  if request.method == 'POST':
    search_query = request.POST["search-query"]
    movies = Movie.objects.filter( Q(title__icontains=search_query) |
                                   Q(synopsis__icontains=search_query)
                                 )
    context["search_query"] = search_query
  else:
    movies = Movie.objects.all()
  
  if filter_form.is_valid():
    if 'critic_score_op' in filter_form.cleaned_data and filter_form.cleaned_data['critic_score_threshold'] is not None:
      movies = movies.critic_score_filter( filter_form.cleaned_data['critic_score_op'], 
                                           filter_form.cleaned_data['critic_score_threshold'])
    if 'audience_score_op' in filter_form.cleaned_data and filter_form.cleaned_data['audience_score_threshold'] is not None:
      movies = movies.audience_score_filter( filter_form.cleaned_data['audience_score_op'], 
                                             filter_form.cleaned_data['audience_score_threshold'])
    if 'runtime_op' in filter_form.cleaned_data and filter_form.cleaned_data['runtime_threshold'] is not None:
      movies = movies.runtime_filter( filter_form.cleaned_data['runtime_op'], 
                                      filter_form.cleaned_data['runtime_threshold'])

  context["movies"] = movies
  return render(request, "starter/movie_list.html", context)

def movie_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  return render(request, "starter/movie_detail.html", {"movie": movie})
