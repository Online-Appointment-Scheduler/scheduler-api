from datetime import datetime
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
        return str(int(value.timestamp()))


class TelegramAuthCreditsSerializer(TokenObtainPairSerializer):
    id = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    photo_url = serializers.CharField()
    auth_date = UnixEpochDateTimeField()
    hash = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def validate(self, attrs):
        attrs.update({'password': ''})
        return super(TelegramAuthCreditsSerializer, self).validate(attrs)
