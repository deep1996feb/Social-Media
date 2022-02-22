from rest_framework import permissions

class hasSelfLikesOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if self.request.method in permissions.SAFE_METHODS:
            return True
        return obj.up_likes_by==request.user or obj.down_likes_by==request.user