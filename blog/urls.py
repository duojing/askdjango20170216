from django.conf.urls import url
from blog import views
from blog import views_cbv

urlpatterns = [
  url(r'^(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
  url(r'^$', views.post_list, name = 'post_list'),
  url(r'^new/$', views.post_new, name = 'post_new'),
  # url(r'^$', views_cbv.post_list, name = 'post_list'),
  # url(r'^new/$', views_cbv.post_new, name = 'post_new'),
  ]