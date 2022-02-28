from django.db import models
from post .models import Post
# Create your models here.

class Likes(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    up_likes_by = models.ForeignKey('auth.User', related_name='up_likes_user', on_delete=models.CASCADE,default=None, blank=True, null=True)
    down_likes_by = models.ForeignKey('auth.User', related_name='down_likes_by', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.post.content




        