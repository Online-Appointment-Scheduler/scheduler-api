from django.urls import include, path
from .views import AuthorizationView
urlpatterns = [
    path('', AuthorizationView.as_view(), name='authorization')
]