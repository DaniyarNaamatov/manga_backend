from rest_framework.exceptions import APIException


class UsernameExistsException(APIException):
    default_code = "username_exists"
    default_detail = "User with the same username already exists"
    status_code = 400
