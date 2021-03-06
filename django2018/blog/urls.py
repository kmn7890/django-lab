from django.conf.urls import url
from . import views, views_cbv

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^cbv/new/$', views_cbv.post_new),
    url(r'^timetest/$', views.test_time, name='timetest'),
]