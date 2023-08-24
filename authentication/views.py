from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import NotTelegramDataError, TelegramDataIsOutdatedError
from django.contrib.auth import authenticate
from .serializers import TelegramAuthCreditsSerializer
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from scheduling.models import Manager
from rest_framework.permissions import AllowAny
from scheduler.settings import AUTH_BOT_TOKEN
from logging import getLogger
from .models import CustomUser
from django.db import IntegrityError
from rest_framework_simplejwt.views import (
    TokenViewBase,
)


logger = getLogger(__name__)


class TelegramAuthView(TokenViewBase):
    serializer_class = TelegramAuthCreditsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Manager.objects.none()

    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            logger.error(f"Failed to validate Telegram auth data with serializer")
            return Response(status=HTTP_400_BAD_REQUEST)
        data = serializer.data
        try:
            verify_telegram_authentication(AUTH_BOT_TOKEN, data)
        except NotTelegramDataError:
            logger.warning(f"Data wasn't generated by Telegram")
            return Response(status=HTTP_400_BAD_REQUEST)
        except TelegramDataIsOutdatedError:
            return Response(status=HTTP_400_BAD_REQUEST)
        telegram_id = data.get("id")
        username = data.get("username")
        user = authenticate(request, telegram_id=telegram_id, username=username)
        if user is None:
            try:
                CustomUser.objects.create_user(telegram_id=telegram_id, username=username)
            except IntegrityError:
                logger.error(f"Tried to create new user with already existing Telegram_id")
                return Response(status=HTTP_400_BAD_REQUEST)
        return Response()
