from rest_framework import serializers
from ..models import Manga, Genre
from users.models import Comment, User


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ("id", "title",)


class ManagaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = (
            "en_name",
            "slug",
            "image",
            "description",
            "chapters_quantity",
            "issue_year",
            "type",
            "genre",
            "likes",
            "views",
            "rating"
        )


class MangaDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Manga
        fields = (
            "en_name",
            "ru_name",
            "image",
            "description",
            "chapters_quantity",
            "issue_year",
            "type",
            "genre",
            "likes",
            "views",
            "rating"
            )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["comments_count"] = instance.manga_comments.count()
        return data
