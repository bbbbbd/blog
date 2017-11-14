# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import markdown
from django.utils.html import strip_tags


# Create your models here.
class Category(models.Model):
    name = models.CharField('分类', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Tag(models.Model):
    name = models.CharField('标签', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Post(models.Model):
    title = models.CharField('标题', max_length=70)
    body = models.TextField('内容')
    created_time = models.DateTimeField('创建时间')
    modified_time = models.DateTimeField('修改时间')
    excerpt = models.CharField('文章摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    author = models.ForeignKey(User, verbose_name='作者')
    views = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'