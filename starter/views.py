from django.shortcuts import render

def landing_page(request):
  return render(request, "starter/movie_list.html")

def movie_detail(request, movie_id):
  return render(request, "starter/movie_detail.html", {"movie_id": movie_id})
