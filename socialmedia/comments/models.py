from django.db import models
from post.models import Post
# Create your models here.

class Comment(models.Model):
    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    comment_image = models.ImageField(upload_to='comment_image', null=True, blank=True)
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment

