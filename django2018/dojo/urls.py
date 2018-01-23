from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^new/$', views.post_new),
    url(r'^new/(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit$', views.post_edit),
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)$', views.hellogongyoo),
    url(r'^list1/$', views.postlist1),
    url(r'^list2/$', views.postlist2),
    url(r'^list3/$', views.postlist3),
    url(r'^excel/$', views.exceldownload),

    url(r'^cbv/list1/$', views_cbv.postlist1),
    url(r'^cbv/list2/$', views_cbv.postlist2),
    url(r'^cbv/list3/$', views_cbv.postlist3),
    url(r'^cbv/excel/$', views_cbv.exceldownload),
]