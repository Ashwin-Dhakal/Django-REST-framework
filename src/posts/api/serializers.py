from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)
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
    user=SerializerMethodField()
    image=SerializerMethodField()
    markdown=SerializerMethodField()


    class Meta:
        model =Post
        fields =[
            'id',
            'title',
            'user',
            'slug',
            'content',
            'markdown',
            'publish',
            'image',
        ]

    def get_markdown(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self,obj):
        try:
            image=obj.image.url
        except:
            image= None
        return image

class PostListSerializer(ModelSerializer):
    url= HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field= 'pk'
    )

    user=SerializerMethodField()
    class Meta:
        model =Post
        fields =[
            'url',
            'title',
            'slug',
            'user',
            'content',

        ]
    def get_user(self, obj):
        return str(obj.user.username)


