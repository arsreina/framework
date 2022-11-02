from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def movies_count(self):
        movies = Movie.objects.filter(director_id=self.id)
        return movies.count() if movies else 0

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField(null=True)
    description = models.TextField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def rating(self):
        reviews = self.reviews.all()
        return sum(i.stars for i in reviews)/len(reviews) if reviews else 'not available'

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(blank=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=[(y, y) for y in range(1, 6)], default=0)

    def __str__(self):
        return self.text
