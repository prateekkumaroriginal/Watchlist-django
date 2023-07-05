from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, Watchlist
from django.views import View

# Create your views here.


class IndexView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/index.html", {
            "movies_currently_watching": movies.filter(watchlist=Watchlist.objects.get(list_name="currently_watching")),
            "movies_on_hold": movies.filter(watchlist=Watchlist.objects.get(list_name="on_hold")),
            "movies_plan_to_watch": movies.filter(watchlist=Watchlist.objects.get(list_name="plan_to_watch")),
            "movies_completed": movies.filter(watchlist=Watchlist.objects.get(list_name="completed")),
        })
