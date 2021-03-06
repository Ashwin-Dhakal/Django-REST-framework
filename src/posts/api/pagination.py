from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,

)

class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4
    max_limit = 10


class PageNumberPagination(PageNumberPagination):
    page_size= 3
