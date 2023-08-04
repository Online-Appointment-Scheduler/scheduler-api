from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from .serializers import TelegramAuthCreditsSerializer
from rest_framework.serializers import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


class TelegramAuthView(APIView):

    def post(self, request) -> Response:
        serializer = TelegramAuthCreditsSerializer(request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            # log
            raise
        validated_date = serializer.validated_data
        jwt_token = ...
        return Response()
        pass
