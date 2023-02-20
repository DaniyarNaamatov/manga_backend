from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from common.exceptions import UsernameExistsException
from .models import User


class UserService:
    model = User

    @classmethod
    def create_user(cls, validated_data):
        if cls.model.objects.filter(username=validated_data["username"]).exists():
            raise UsernameExistsException()

        return cls.model.objects._create_user(**validated_data)

    @classmethod
    def generate_token(cls, user: model) -> dict:
        access = AccessToken.for_user(user)
        refresh = AccessToken.for_user(user)
        data = {
            "message": "Login successfully",
            "user": user.username,
            "access_token": str(access),
            "refresh_token": str(refresh),
        }
        return data
