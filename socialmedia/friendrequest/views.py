
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from user_profile.models import UserProfile
from .serializers import FriendSerializer 
from .models import FriendRequest
from django.contrib.messages import constants as messages

class SendFriendRequestViewSet(viewsets.ModelViewSet):

    def get(self, request, *args, **kwargs):
        queryset = request.GET.get('profile_id')
        queryset = request.GET.get('request_id')
        target = UserProfile.objects.get(id=queryset)
        requester = UserProfile.objects.get(id=queryset)
        target.send_friend_request(requester)
        message = 'Friend request to {} sent!'.format(target.visible_name)
        messages.info(request, message)
        return redirect('profile', username=target.user.username)


class AddFriendViewSet(viewsets.ModelViewSet):

    def get(self, request, *args, **kwargs):
        try:
            profile_id = request.GET.get('profile_id')
            requester_id = request.GET.get('requester_id')
            queryset = UserProfile.objects.get(id=profile_id)
            requester = UserProfile.objects.get(id=requester_id)
            queryset.add_friend(requester)
            message = 'Added friend {}!'.format(queryset.visible_name)
            messages.info(request, message)
            return redirect('friends', username=queryset.user.username)
        except Exception as e:
            print('Error: {}'.format(e))


