from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    list_name = models.CharField(max_length=20)

    def __str__(self):
        return self.list_name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(2100),
    ])
    duration_in_min = models.PositiveSmallIntegerField()
    imdb_rating = models.DecimalField(max_digits=2, decimal_places=1)
    rotten_tomatoes_score = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    cover_img = models.ImageField(upload_to="cover_images")
    tags = models.ManyToManyField(Tag)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.SET_NULL, null=True, blank=True, related_name="movies")
    
    def get_absolute_url(self):
        return reverse("movie-detail", args=[self.pk])

    def __str__(self):
        return self.title
