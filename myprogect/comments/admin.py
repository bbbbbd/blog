# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Comment
from django.contrib import admin

# Register your models here.
# admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_time')

