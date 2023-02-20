from django.urls import path
from .views import MangaListApiView


urlpatterns = [
    path("manga-list", MangaListApiView.as_view(), name="manga-list")
]