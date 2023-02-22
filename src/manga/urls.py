from django.urls import path
from .views import MangaListApiView, MangaCommentsView, MangaDetailView
from users.views import AddToFavorite


urlpatterns = [
    path("manga/", MangaListApiView.as_view(), name="manga-list"),
    path("manga/<str:slug>/", MangaDetailView.as_view(), name="manga-detail"),
    path("manga/<str:slug>/comments/", MangaCommentsView.as_view()),
    path("manga/<str:slug>/favorite/", AddToFavorite.as_view(), name="add-to"),
]
