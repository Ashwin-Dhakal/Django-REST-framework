from rest_framework.generics import ListAPIView
from posts.models import Post #..model gare pani hunthyo tara post.model garda ahjai ramro

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    
