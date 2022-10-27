from rest_framework import serializers
from movie_app.models import Review, Director, Movie


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title duration director description'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id movie_id text stars'.split()


class MovieReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class MovieWithReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title reviews rating'.split()

    reviews = MovieReviewsSerializer(many=True)
