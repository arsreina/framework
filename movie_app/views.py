from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, ReviewSerializer, MovieSerializer, \
    MovieWithReviewsSerializer, MovieCreateSerializer, DirectorCreateSerializer, \
    DirectorUpdateSerializer, MovieUpdateSerializer, ReviewValidateAbstractSerializer, ReviewUpdateSerializer
from .models import Director, Review, Movie
from rest_framework import status


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = DirectorCreateSerializer(data=request.data)
        if serializer.is_valid():
            director = Director.objects.create(
                **serializer.validated_data
            ).save()
            return Response(data=DirectorSerializer(director).data,
                            status=status.HTTP_201_CREATED)
        return serializer.is_valid(raise_exception=True)


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
        serializer = DirectorUpdateSerializer(data=request.data,
                                              context={'id': id})
        if serializer.is_valid():
            director.name = serializer.validated_data.get('name')
            director.save()
            return Response(data=DirectorSerializer(director).data,
                            status=status.HTTP_202_ACCEPTED)
        return serializer.is_valid(raise_exception=True)


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieCreateSerializer(data=request.data)
        if serializer.is_valid():
            movie = Movie.objects.create(
                **serializer.validated_data
            ).save()
            return Response(data=MovieSerializer(movie).data,
                            status=status.HTTP_201_CREATED)
        return serializer.is_valid(raise_exception=True)


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
        serializer = MovieUpdateSerializer(data=request.data,
                                           context={'id': id})
        if serializer.is_valid():
            movie.title = serializer.validated_data.get('title')
            movie.description = serializer.validated_data.get('description')
            movie.duration = serializer.validated_data.get('duration')
            movie.director_id = serializer.validated_data.get('director_id')
            movie.save()
            return Response(data=MovieSerializer(movie).data,
                            status=status.HTTP_202_ACCEPTED)
        return serializer.is_valid(raise_exception=True)


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ReviewValidateAbstractSerializer(data=request.data)
        if serializer.is_valid():
            review = Review.objects.create(
                **serializer.validated_data
            )
            return Response(data=ReviewSerializer(review).data,
                            status=status.HTTP_201_CREATED)
        return serializer.is_valid(raise_exception=True)


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
        serializer = ReviewUpdateSerializer(data=request.data,
                                            context={'id': id})
        if serializer.is_valid():
            review.text = serializer.validated_data.get('text')
            review.movie_id = serializer.validated_data.get('movie_id')
            review.stars = serializer.validated_data.get('stars')
            review.save()
            return Response(data=ReviewSerializer(review).data,
                            status=status.HTTP_202_ACCEPTED)
        return serializer.is_valid(raise_exception=True)

