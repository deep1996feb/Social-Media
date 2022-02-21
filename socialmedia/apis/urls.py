from posixpath import basename
from tokenize import Pointfloat
from rest_framework.routers import DefaultRouter
from more.views import UserViewset
from user_profile.views import Profileviewset
from post.views import PostviewSet

router = DefaultRouter()
router.register('more', UserViewset, basename='more')
router.register('profiles', Profileviewset)
router.register('posts', PostviewSet)
urlpatterns = router.urls

