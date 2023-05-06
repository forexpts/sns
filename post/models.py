from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='post_owner'
        )
    
    content = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    favorite_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='', blank=True, null=True)
    VISIBILITY_CHOICES = [
        ('public', '公開'),
        ('private', '非公開'),
    ]
    visibility = models.CharField(
        max_length=10,
        choices=VISIBILITY_CHOICES, 
        default='public'
    )

    class Meta:
        ordering = ['-created_at']

class Favorite(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorite_owner'
    )

    content_id = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )