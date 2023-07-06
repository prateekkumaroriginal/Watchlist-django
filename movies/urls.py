from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.MovieDetailView.as_view(), name="movie-detail"),
    path("all-movies", views.AllMoviesView.as_view(), name="all-movies"),
]
