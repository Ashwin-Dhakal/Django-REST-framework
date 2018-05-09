from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from comments.api.serializers import CommentSerializer
from comments.models import Comment


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
    comments=SerializerMethodField()
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
            'comments',
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

    def get_comments(self, obj):
        # content_type= obj.get_content_type
        # object_id=obj.id
        c_qs=Comment.objects.filter_by_instance(obj)
        comments=CommentSerializer(c_qs, many=True).data
        return comments


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


