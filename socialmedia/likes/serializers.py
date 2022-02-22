from numpy import source
from .models import Likes
from rest_framework import serializers

class LikesSerializer(serializers.ModelSerializer):
    up_likes_by = serializers.ReadOnlyField(source='up_likes_by.username')
    down_likes_by = serializers.ReadOnlyField(source='down_likes_by.username')

    class Meta:
        model = Likes
        fields = ('id', 'post', 'up_likes_by', 'down_likes_by')