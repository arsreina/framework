import django.db.utils
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, ReviewSerializer, MovieSerializer, MovieWithReviewsSerializer
from .models import Director, Review, Movie
from rest_framework import status


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        director = Director.objects.create(
            **request.data
        ).save()
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not found'})
    if request.method == 'GET':
        return Response(data=DirectorSerializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        try:
            movie = Movie.objects.create(
                **request.data
            ).save()
        except django.db.utils.IntegrityError:
            return Response(data='No director with such id')
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movies_with_reviews_view(request):
    movies = Movie.objects.all()
    serializer = MovieWithReviewsSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found'})
    if request.method == 'GET':
        return Response(data=MovieSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        movie.title = request.data.get('title')
        movie.duration = request.data.get('duration')
        movie.director = request.data.get('director_id')
        movie.description = request.data.get('description')
        movie.save()
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        try:
            review = Review.objects.create(
                **request.data
            ).save()
        except django.db.utils.IntegrityError:
            return Response(data='No movie with such id',
                            status=status.HTTP_404_NOT_FOUND)
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    if request.method == 'GET':
        return Response(data=ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        fields = request.data
        review.movie = request.data.get('movie_id')
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_202_ACCEPTED)

