from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','created_at','updated_at']

# admin.site.register(Post, PostAdmin) #커스텀한 어드민 등록

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass