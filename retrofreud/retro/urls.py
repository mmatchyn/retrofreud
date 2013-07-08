from django.conf.urls import patterns, url
from retro import views

urlpatterns = patterns('retro.views',
	url(r'^$', 'index'),
	url(r'^close/(?P<id>\d+)/$', 'close'),
	url(r'^open/(?P<id>\d+)/$', 'reopen'),
	url(r'^vote/(?P<id>\d+)/$', 'vote'),
	url(r'^update/(?P<id>\d+)/$', 'update'),
	url(r'^(?P<id>\d+)/$', 'issue'),
)