from rest_framework import serializers
from ..models import User, Comment


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=5, max_length=35)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=50)
    phone = serializers.CharField(min_length=13, max_length=13)
    image_file = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "phone",
            "email",
            "password",
            "image_file",
        )


class SignInSerializer(serializers.Serializer):
    login = serializers.CharField(min_length=5, max_length=35)
    password = serializers.CharField(min_length=8, max_length=50)
