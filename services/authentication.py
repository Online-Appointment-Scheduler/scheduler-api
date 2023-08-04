from authentication.serializers import TelegramAuthCreditsSerializer
from scheduler.settings import AUTH_BOT_TOKEN
import hashlib
import hmac
import binascii


def telegram_auth_to_data_check_string(data: dict) -> str:
    key_to_values = data.items()
    data_check_string = '\n'.join(list(map(lambda key_to_value: key_to_value[0] + '=' + key_to_value[1], key_to_values)))
    return data_check_string


def validate_auth_telegram(data_check_string, telegram_hash: str):
    secret_key = hashlib.sha256(AUTH_BOT_TOKEN.encode()).digest()
    hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).digest()
    own_hash = binascii.hexlify(hmac_hash).decode()
    if own_hash == telegram_hash:
        return True
    return False
