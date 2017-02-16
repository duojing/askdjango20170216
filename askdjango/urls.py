"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.shortcuts import redirect
from blog import views as blog_views
#from webtoon import views as webtoon_views  #그냥 views라고 하면 덮어쓰기 되므로.

#def root(request):
#    return redirect('post_list')
# 한 번만 쓸 함수니까 lambda로 써줘도 ok.

urlpatterns = [
    #url(r'^$', root)
    url(r'^$', lambda request: redirect('blog:post_list')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')), #namespace를 걸지 않는다.
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^webtoon/', include('webtoon.urls', namespace='webtoon')),
    url(r'^game/', include('game.urls', namespace='game')),
    url(r'^journal/', include('journal.urls', namespace='journal')),
    url(r'^now/$', blog_views.current_datetime),
    url(r'^hello/(?P<name>[ㄱ-힣])/(?P<age>\d+)/$',blog_views.name_and_age),
    #정규표현식은 ""아닌 []
    url(r'^sum/(?P<x>[0-9/]+)/$', blog_views.mysum),


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
