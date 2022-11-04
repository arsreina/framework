from rest_framework import serializers
from movie_app.models import Review, Director, Movie
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class DirectorValidateAbstractSerializer(DirectorSerializer, serializers.Serializer):
    name = serializers.CharField(min_length=1)


class DirectorCreateSerializer(DirectorValidateAbstractSerializer):

    def validate_name(self, name):
        try:
            Director.objects.get(name=name)
        except Director.DoesNotExist:
            return name
        raise ValidationError('Director with this name already exists')


class DirectorUpdateSerializer(DirectorValidateAbstractSerializer):

    def validate_name(self, name):
        try:
            Director.objects.exclude(id=self.context.get('id')).get(name=name)
        except Director.DoesNotExist:
            return name
        raise ValidationError('Director with this name already exists')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title duration director description'.split()


class MovieValidateAbstractSerializer(MovieSerializer, serializers.Serializer):
    title = serializers.CharField(min_length=1)
    duration = serializers.IntegerField(required=False, max_value=500)
    description = serializers.CharField(required=False)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('No director with such id')
        return director_id


class MovieCreateSerializer(MovieValidateAbstractSerializer):

    def validate_title(self, title):
        try:
            Movie.objects.get(title=title)
        except Movie.DoesNotExist:
            return title
        raise ValidationError('This title has already been used')

    def validate_description(self, description):
        try:
            Movie.objects.get(description=description)
        except Movie.DoesNotExist:
            return description
        raise ValidationError('Movie with this description already exists')


class MovieUpdateSerializer(MovieValidateAbstractSerializer):

    def validate_id(self):
        try:
            Movie.objects.get(id=self.context.get('id'))
        except Movie.DoesNotExist:
            raise ValidationError('No movie with such id')
        return self.context.get('id')

    def validate_title(self, title):
        try:
            Movie.objects.exclude(id=self.context.get('id')).get(title=title)
        except Movie.DoesNotExist:
            return title
        raise ValidationError('This title has already been used')

    def validate_description(self, description):
        try:
            Movie.objects.exclude(id=self.context.get('id')).get(description=description)
        except Movie.DoesNotExist:
            return description
        raise ValidationError('Movie with this description already exists')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id movie_id text stars'.split()


class ReviewValidateAbstractSerializer(ReviewSerializer, serializers.Serializer):
    text = serializers.CharField(min_length=1, max_length=1000)
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('No movie with such id')
        return movie_id

    def validate_stars(self, stars):
        if stars < 1 or stars > 5:
            raise ValidationError('Invalid value')
        return stars


class ReviewCreateSerializer(ReviewValidateAbstractSerializer):
    pass


class ReviewUpdateSerializer(ReviewValidateAbstractSerializer):

    def validate_id(self):
        try:
            Review.objects.get(id=self.context.get('id'))
        except Review.DoesNotExist:
            raise ValidationError('No review with such id')
        return self.context.get('id')


class MovieReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class MovieWithReviewsSerializer(serializers.ModelSerializer):
    reviews = MovieReviewsSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title reviews rating'.split()
