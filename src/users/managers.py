from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, phone, image, password, **extra):
        user = self.model(username=username, phone=phone, image=image, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, phone, image, password):
        return self._create_user(username, phone, image, password)

    def create_superuser(self, username, password):
        return self._create_user(username, password, is_superuser=True, is_staff=True)