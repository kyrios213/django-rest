from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('id/<id>', views.ImageAPIView.as_view(), name="api_image"),
]
