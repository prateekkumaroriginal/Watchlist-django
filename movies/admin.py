from django.contrib import admin
from .models import Movie, Tag, Watchlist

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_filter = ("tags", "watchlist")
    list_display = ("title", "release_year")


admin.site.register(Movie, MovieAdmin)
admin.site.register(Tag)
admin.site.register(Watchlist)