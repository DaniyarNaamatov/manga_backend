from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    phone = PhoneNumberField(null=True, blank=True, verbose_name="Номер телефона")
    image = models.URLField(null=True, blank=True, verbose_name="Ссылка на картинку из другого источника")
    image_file = models.ImageField(
        default="default_media/avatar.jpg",
        upload_to="uploaded_media",
        null=True,
        blank=True,
        verbose_name="Картинка"
    )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Комментатор")
    manga = models.ForeignKey(
        "manga.Manga", on_delete=models.CASCADE, related_name="manga_comments",
        verbose_name="Манга"
    )
    text = models.CharField(max_length=255, null=False, blank=False, verbose_name="Текст")

    def __str__(self):
        return f"{self.user} Прокомментровал {self.manga}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

