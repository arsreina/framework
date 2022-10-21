from django.contrib import admin
from movie_app.models import Review, Director, Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = 'title duration description director'.split()
    search_fields = 'director'.split()


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
admin.site.register(Review)
