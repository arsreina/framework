from rest_framework import serializers
from movie_app.models import Review, Director, Movie


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title duration director description'.split()


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class MovieWithReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()

    reviews = ReviewsSerializer(many=True)
