from datetime import datetime
from rest_framework import serializers
from services.authentication import validate_auth_telegram, telegram_auth_to_data_check_string
from rest_framework.serializers import ValidationError


class UnixEpochDateTimeField(serializers.DateTimeField):
    def to_internal_value(self, data):
        # Convert Unix epoch time to datetime object
        try:
            epoch_time = int(data)
            return datetime.fromtimestamp(epoch_time)
        except (ValueError, TypeError):
            raise serializers.ValidationError("Invalid Unix epoch time")

    def to_representation(self, value):
        # Convert datetime object to Unix epoch time
        if value is None:
            return None
        return str(value.timestamp())


class TelegramAuthCreditsSerializer(serializers.Serializer):
    id = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    photo_url = serializers.CharField()
    auth_date = UnixEpochDateTimeField()
    hash = serializers.CharField()