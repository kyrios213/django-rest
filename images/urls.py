from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'images'

urlpatterns = [
    path('', TemplateView.as_view(template_name='images/index.html')),
    path('images/', views.ImagesListView.as_view(), name='images'),
]
