from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


class MockSerializer(serializers.Serializer):
    ...


class AuthorizationView(RetrieveAPIView, CreateAPIView, GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MockSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK, template_name='auth.html')

    def create(self, request, *args, **kwargs):
        return Response(data=request.POST)

