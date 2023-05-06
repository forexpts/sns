from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class Account(AbstractUser):
    avator = models.ImageField(upload_to='', null=True)

    following_count = models.IntegerField(default=0)
    follower_count = models.IntegerField(default=0)

class Follow(models.Model):
    follow_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='follow_owner'
    )

    follower_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )