from rest_framework.generics import ListAPIView
from posts.models import Post #..model gare pani hunthyo tara post.model garda ahjai ramro

from .serializers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

