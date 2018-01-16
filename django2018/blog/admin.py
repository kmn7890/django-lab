from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','content_size','status','created_at','updated_at']
    actions = ['make_available','make_denied','make_contracted','make_finished']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_available(self, request, queryset):
        updated_count=queryset.update(status='available') #QuerySet.update
        self.message_user(request, '{}건의 포스팅을 available 상태로 변경'.format(updated_count))
    make_available.short_description = '선택 포스팅 available 상태로 변경'

    def make_denied(self, request, queryset):
        updated_count=queryset.update(status='denied') #QuerySet.update
        self.message_user(request, '{}건의 포스팅을 denied 상태로 변경'.format(updated_count))
    make_denied.short_description = '선택 포스팅 denied 상태로 변경'

    def make_contracted(self, request, queryset):
        updated_count=queryset.update(status='contracted') #QuerySet.update
        self.message_user(request, '{}건의 포스팅을 contracted 상태로 변경'.format(updated_count))
    make_contracted.short_description = '선택 포스팅 contracted 상태로 변경'

    def make_finished(self, request, queryset):
        updated_count=queryset.update(status='finished') #QuerySet.update
        self.message_user(request, '{}건의 포스팅을 finished 상태로 변경'.format(updated_count))
    make_finished.short_description = '지정 포스팅 finished 상태로 변경'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

