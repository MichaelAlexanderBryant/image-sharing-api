from rest_framework import generics

from .models import Post, Comment
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, MyTokenObtainPairSerializer, CommentSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserPostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer
    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user)
    
class UserPostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer
    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user)
    
class CommentListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = CommentSerializer
    def get_queryset(self):
        current_url = self.request.get_full_path()
        post_id = current_url[current_url.find('comments/')+9:-1]
        return Comment.objects.filter(post_id=post_id)