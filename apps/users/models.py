from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(_('Phone number'), max_length=15)
    date_of_birth = models.CharField(_('Date of birth'), max_length=10, blank=True, null=True)
    bio = models.CharField(_('Bio'), max_length=255, blank=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    address = models.CharField(_('Address'), max_length=255)
    avatar = models.ImageField(upload_to='avatars/')
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f"{self.user.username}'s profile"
