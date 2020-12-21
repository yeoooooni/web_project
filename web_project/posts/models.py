from django.utils import timezone
from django.db import models
#from django.urls import revers


class Post(models.Model):

    POST_TYPE = [
        (0, "해킹"),
        (1, "개발"),
        (2, "보안"),
        (3, "책")
    ]

    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(null=False, verbose_name="내용")
    view_count = models.IntegerField(default=0, verbose_name="조회수")
    image = models.ImageField(upload_to="posts/img", blank=True, default="posts/default/default_post_image.jpy")
    file = models.FileField(upload_to="posts/file", blank=True)
    link = models.URLField(null=True, blank=True, verbose_name="참조링크")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트시간")
    post_type = models.PositiveSmallIntegerField(choices=POST_TYPE, verbose_name="게시글타입")



