from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email' # to make sure that the email is used in place of the username
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self) -> str:
        return self.username
