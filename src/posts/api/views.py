from rest_framework.generics import ListAPIView, RetrieveAPIView
from posts.models import Post #..model gare pani hunthyo tara post.model garda ahjai ramro

from .serializers import PostDetailSerializer, PostListSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer



