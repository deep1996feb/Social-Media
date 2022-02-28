from django.shortcuts import render, get_object_or_404
from post .models import Post
from likes .permission import  hasSelfLikesOrReadOnly
from rest_framework import viewsets, status, permissions
from .models import Likes
from .serializers import LikesSerializer
# Create your views here.

class LikesViewSet(viewsets.ModelViewSet):
    queryset=Likes.objects.all()
    serializer_class=LikesSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly, hasSelfLikesOrReadOnly]
    def perform_create(self, serializer):
        post_instance=get_object_or_404(Post,pk=self.request.data['post'])

       
        if self.request.data['up_likes']:
            already_up_likes=Likes.objects.filter(post=post_instance,up_likes_by=self.request.user).exists()
            if already_up_likes:
                raise serializer.ValidationError({"message":"You have already liked this post"})
            else:
                serializer.save(up_likes_by=self.request.user,post=post_instance)
       
        else:
            already_down_voted=Likes.objects.filter(post=post_instance,down_likes_by=self.request.user).exists()
            if already_down_voted:
                raise serializer.ValidationError({"message":"You have already disliked this post"})
            else:
                serializer.save(down_likes_by=self.request.user,post=post_instance)
 