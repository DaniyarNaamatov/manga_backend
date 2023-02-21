from django.urls import path
from .views import SignInView, SignUpView, AddToFavoriteSerializer, ProfileView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path("profile/<int:id>/", ProfileView.as_view())
]
