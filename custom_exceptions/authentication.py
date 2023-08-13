class TelegramIdAbsentException(Exception):
    def __init__(self, message="Tried to send an absent message"):
        super().__init__(message)


class UsernameAbsentException(Exception):
    def __init__(self, message="Tried to send an absent message"):
        super().__init__(message)