from django.shortcuts import render, get_object_or_404
from rest_framework import generics, response, status
from .models import Manga
from manga.api.serializers import (
    ManagaSerializer,
    CommentSerializer,
    CommentAddSerializer,
)


class MangaListApiView(generics.ListAPIView):
    queryset = Manga.objects.filter(is_deleted=False)
    serializer_class = ManagaSerializer


class MangaCommentsView(generics.GenericAPIView):
    serializer_class = CommentSerializer

    def get(self, request, slug):
        manga = get_object_or_404(Manga, slug=slug)
        comments_data = self.serializer_class(
            manga.manga_comments, many=True, context={"request": request}
        ).data

        return response.Response(data=comments_data)

    def post(self, request, slug):
        if request.user.is_authenticated:
            manga = get_object_or_404(Manga, slug=slug)
            serializer = CommentAddSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    manga=manga, user=request.user, text=request.data["text"]
                )
                return response.Response(
                    data={
                        "message": "Comment sent successfully",
                        "text": self.request.data["text"],
                    },
                    status=status.HTTP_201_CREATED,
                )
        return response.Response(
            data={"message": "Not authorized error"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


# Create your views here.
