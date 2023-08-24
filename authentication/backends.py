from django.contrib.auth.backends import ModelBackend

from authentication.models import CustomUser
from custom_exceptions.authentication import TelegramIdAbsentException, UsernameAbsentException
from logging import getLogger

logger = getLogger()

class TelegramAuthBackend(ModelBackend):

    def authenticate(self, request, telegram_id, username, **kwargs):
        if telegram_id is None:
            telegram_id = request.data.get("telegram_id", '')
            if telegram_id == '':
                raise TelegramIdAbsentException("Telegram_id wasn't present in the payload")
        if username is None:
            username = request.data.get('username', '')
            if username == '':
                raise UsernameAbsentException("username wasn't present in the payload")
        try:
            return CustomUser.objects.get(telegram_id=telegram_id, username=username)
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, telegram_id, username):
        try:
            return CustomUser.objects.get(pk=telegram_id, username=username)
        except CustomUser.DoesNotExist:
            return None
