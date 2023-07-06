from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import Movie, Watchlist
from django.views import View
from django.views.generic import DetailView
from django.urls import reverse
import json

# Create your views here.


class IndexView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/index.html", {
            "movies_currently_watching": movies.filter(watchlist=Watchlist.objects.get(list_name="currently_watching")),
            "movies_on_hold": movies.filter(watchlist=Watchlist.objects.get(list_name="on_hold")),
            "movies_plan_to_watch": movies.filter(watchlist=Watchlist.objects.get(list_name="plan_to_watch")),
            "movies_completed": movies.filter(watchlist=Watchlist.objects.get(list_name="completed")),
            "all_movies": movies
        })

    def post(self, request):
        data = request.POST
        movie = Movie.objects.get(id=int(data['movie']))
        if data['change-action'] == 'remove':
            try:
                movie.watchlist.movies.remove(movie)
            except:
                pass
        else:
            new_watchlist = get_object_or_404(
                Watchlist, list_name=data['change-action'])
            new_watchlist.movies.add(movie)
        return HttpResponseRedirect(reverse("movies:index"))
    
class MovieDetailView(DetailView):
    model = Movie

