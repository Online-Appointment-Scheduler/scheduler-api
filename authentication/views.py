from rest_framework.generics import CreateAPIView
from django_telegram_login.authentication import verify_telegram_authentication
from .serializers import TelegramAuthCreditsSerializer
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from scheduling.models import Manager
from rest_framework.permissions import AllowAny
from scheduler.settings import AUTH_BOT_TOKEN


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
        verify_telegram_authentication(AUTH_BOT_TOKEN, data)
        return Response()
        pass
