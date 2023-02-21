from rest_framework.exceptions import APIException


class UsernameExistsException(APIException):
    default_code = "username_exists"
    default_detail = "User with the same username already exists"
    status_code = 400


class FavoriteMangaExists(APIException):
    default_code = "favorite_manga_exists"
    default_detail = "The manga is already in my favorites"
    status_code = 400
