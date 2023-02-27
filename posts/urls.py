from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import PostList, PostDetail, MyTokenObtainPairView, UserPostList, UserPostDetail, CommentListView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("comments/<int:pk>/", CommentListView.as_view(), name="comment_list"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("yourposts/", UserPostList.as_view(), name="userpost_list"),
    path("yourposts/<int:pk>", UserPostDetail.as_view(), name="userpost_detail"),
    path("", PostList.as_view(), name="post_list")
]