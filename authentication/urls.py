from django.urls import include, path
from django.views.generic import TemplateView
from .views import TelegramAuthView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('telegram/', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='auth.html'), name='authentication'),
    path('token/', TelegramAuthView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]