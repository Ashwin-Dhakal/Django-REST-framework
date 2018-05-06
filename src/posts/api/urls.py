from django.conf.urls import url
from django.contrib import admin

from .views import (   #similar to post.api.views
        PostListAPIView
        )



urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
    # url(r'^create/$', post_create),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]
