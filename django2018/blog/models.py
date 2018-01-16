import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^([+-]\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid lng/lat type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('available','available'),
        ('contracted','contracted'),
        ('denied','denied'),
        ('finished','finished'),
    )
    author = models.CharField(max_length=20, default='Mina Kang', choices=(
                              ('mina','Mina Kang'),
                              ('manjun','Manjun Gim'),
                              ('seunghun','Seunghun Shin'),
                              ('jaeyoon','Jaeyoon Song'),
                              ),
                              verbose_name='author as a team member')
    category = models.IntegerField(choices=(
                             (1,'Mission'),
                             (2,'Studies'),
                             (3,'Daily SSTNS'),
                             ), default=0)
    title = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    content = models.TextField()
    tags = models.CharField(max_length=100, blank = True)
    lnglat = models.CharField(max_length=50, blank=True, validators=[lnglat_validator], help_text='경도/위도 포맷으로 넣어주세요')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name