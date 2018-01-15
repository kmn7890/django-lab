from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','author','title','content_size','created_at','updated_at']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))

    content_size.short_description = '글자수'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass