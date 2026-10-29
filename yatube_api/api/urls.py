from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register(r'v1/posts', PostViewSet, basename='posts')
router.register(r'v1/groups', GroupViewSet, basename='groups')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
]
