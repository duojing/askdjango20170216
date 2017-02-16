from django.conf.urls import url
from journal import views

urlpatterns = [
  url(r'^(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
  url(r'^$', views.post_list, name = 'post_list'),
  url(r'^new/$', views.post_new, name = 'post_new'),
  ]