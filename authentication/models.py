from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, username, telegram_id, **extra_fields):
        if not username:
            raise ValueError(_('The Username field must be set'))
        if not telegram_id:
            raise ValueError(_('The Telegram id field must be set'))
        user = self.model(telegram_id=telegram_id, username=username, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, telegram_id, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, telegram_id, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=70, blank=True, null=True)
    last_name = models.CharField(max_length=70, blank=True, null=True)
    password = None

    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['telegram_id']

    def __str__(self):
        return self.username
