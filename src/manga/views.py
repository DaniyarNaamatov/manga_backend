from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Manga
from manga.api.serializers import ManagaSerializer


class MangaListApiView(generics.ListAPIView):
    queryset = Manga.objects.filter(is_deleted=False)
    serializer_class = ManagaSerializer


# Create your views here.
