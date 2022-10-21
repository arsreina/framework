from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer
from .models import Director, Review, Movie


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    serializer = DirectorSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    serializer = DirectorSerializer(reviews, many=True)
    return Response(data=serializer.data)
