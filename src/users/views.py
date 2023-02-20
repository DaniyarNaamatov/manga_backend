from rest_framework import generics, response, status
from django.contrib.auth import authenticate

from .models import User, Comment
from .services import UserService
from users.api.serializers import SignInSerializer, SignUpSerializer


class SignUpView(generics.CreateAPIView):
    queryset = UserService.model.objects.all()
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            UserService.create_user(serializer.validated_data)
            return response.Response(
                data={"message": "Register successfully"},
                status=status.HTTP_201_CREATED,
            )
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInView(generics.GenericAPIView):
    queryset = UserService.model.objects.filter(is_deleted=False).filter(
        is_active=False
    )
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.data["login"], password=serializer.data["password"]
            )
            return response.Response(
                data=UserService.generate_token(user=user), status=status.HTTP_200_OK
            )

        return response.Response(data=serializer.errors)
