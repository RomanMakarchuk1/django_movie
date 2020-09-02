from django.contrib import admin
from .models import Movie, Genre, Rating, RatingStar, Actor, Reviews, Category, MovieShots


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Actor)
admin.site.register(Reviews)
admin.site.register(Category)
admin.site.register(MovieShots)


