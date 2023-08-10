from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, CreateAPIView, GenericAPIView
from rest_framework.views import APIView

from services.authentication import telegram_auth_to_data_check_string, validate_auth_telegram
from .serializers import TelegramAuthCreditsSerializer
from rest_framework.serializers import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from scheduling.models import Manager
from rest_framework.permissions import AllowAny


class TelegramAuthView(CreateAPIView):
    serializer_class = TelegramAuthCreditsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Manager.objects.none()

    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            # log
            raise
        data = serializer.data
        data_check_string = telegram_auth_to_data_check_string(data)
        if not validate_auth_telegram(data_check_string, data["hash"]):
            raise ValidationError("The hash wasn't originated from Telegram. The auth data and its hash are different "
                                  "or the secret is invalid")
        jwt_token = RefreshToken.for_user(data)
        return Response(jwt_token, )
        pass
