# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blog.models import Post


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    email = models.EmailField(max_length=255, verbose_name='邮箱')
    url = models.URLField(blank=True, verbose_name='地址', help_text='可为空')
    text = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    post = models.ForeignKey(Post, verbose_name='文章标题')

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'