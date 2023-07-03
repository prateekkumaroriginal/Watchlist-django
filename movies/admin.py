from django.contrib import admin
from .models import Movie, Tag, Watchlist

# Register your models here.

admin.site.register(Movie)
admin.site.register(Tag)
admin.site.register(Watchlist)