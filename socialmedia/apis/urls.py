from posixpath import basename
from tokenize import Pointfloat
from rest_framework.routers import DefaultRouter
from comments.views import CommentviewSet
from more.views import UserViewset
from user_profile.views import Profileviewset
from post.views import PostviewSet
from comments.views import CommentviewSet
from likes.views import LikesViewSet
from friendrequest.views import SendFriendRequestViewSet
router = DefaultRouter()
router.register('more', UserViewset, basename='more')
router.register('profiles', Profileviewset)
router.register('posts', PostviewSet)
router.register('comments', CommentviewSet)
router.register('likes', LikesViewSet)
router.register('sendrequest', SendFriendRequestViewSet, basename='sendrequest')
urlpatterns = router.urls


