from .models import FriendRequest
from rest_framework import serializers

class FriendSerializer(serializers.ModelSerializer):
     owner = serializers.ReadOnlyField(source='owner.username')
   
     class Meta:
         model = FriendRequest
         fields = '__all__'