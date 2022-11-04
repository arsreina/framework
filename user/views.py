from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserLoginSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView


class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key},
                            status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(
            **serializer.validated_data
        )
        return Response(status=status.HTTP_201_CREATED)
