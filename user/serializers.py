from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserAbstractSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=1)
    password = serializers.CharField(min_length=3)


class UserLoginSerializer(UserAbstractSerializer):
    pass


class UserRegistrationSerializer(UserAbstractSerializer):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise ValidationError('User with this username already exists')

