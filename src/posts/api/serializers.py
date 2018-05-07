from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model =Post
        fields =[
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]


class PostListSerializer(ModelSerializer):
    url= HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field= 'pk'
    )
    delete_url= HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field= 'pk'
    )
    class Meta:
        model =Post
        fields =[
            'url',
            'title',
            'slug',
            'content',
            'publish',
            'delete_url',
        ]

