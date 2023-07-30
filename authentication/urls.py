from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('telegram/', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='auth.html'), name='authentication'),
]