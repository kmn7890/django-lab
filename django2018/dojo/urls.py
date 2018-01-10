from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)$', views.hellogongyoo),
    url(r'^list1/$', views.postlist1),
    url(r'^list2/$', views.postlist2),
    url(r'^list3/$', views.postlist3),
    url(r'^excel/$', views.exceldownload),
]