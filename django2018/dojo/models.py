from django import forms
from django.db import models
from django.shortcuts import reverse

# Create your models here. 데이터베이스에 저장되는 데이터 타입을 만듦. 길이 제한이 있는 문자열과 없는 문자열로 구분됨.

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField(validators=[min_length_3_validator])
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dojo:post_detail', args=['self.id'])