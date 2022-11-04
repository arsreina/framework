from .serializers import MovieWithReviewsSerializer, MovieCreateSerializer, DirectorCreateSerializer, \
    DirectorUpdateSerializer, MovieUpdateSerializer, ReviewCreateSerializer, ReviewUpdateSerializer
from .models import Director, Review, Movie
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorCreateSerializer


class DirectorItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    lookup_field = 'id'
    serializer_class = DirectorUpdateSerializer


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer


class MovieItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    lookup_field = 'id'
    serializer_class = MovieUpdateSerializer


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer


class ReviewItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    lookup_field = 'id'
    serializer_class = ReviewUpdateSerializer


class MovieWithReviewsListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieWithReviewsSerializer
