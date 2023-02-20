from django.urls import path
from .views import MangaListApiView, MangaCommentsView


urlpatterns = [
    path("manga-list/", MangaListApiView.as_view(), name="manga-list"),
    path("manga-list/<str:slug>/comments/", MangaCommentsView.as_view()),
]
