from django.db.models import query
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response

from .renderers import *
from images.models import Images

# Create your views here.
def test(request):
    return JsonResponse({'test': 'test'})


class ImageAPIView(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        queryset = Images.objects.get(id=self.kwargs['id']).image
        data = queryset
        return Response(data, content_type='image/jpg')

