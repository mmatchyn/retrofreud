from django.conf.urls import patterns, url
from moodmeter import views

urlpatterns = patterns('moodmeter.views',
	url(r'^(?P<id>\d+)/$', 'profile'),
	url(r'^update/(?P<id>\d+)/$', 'update'),
	url(r'^vote/thumb/(?P<id>\d+)/$', 'vote_thumb'),
	url(r'^vote/(?P<id>\d+)/$', 'vote'),
	url(r'^(?P<action>\w+)/(?P<id>\d+)/$', 'profile'),
	url(r'^$', 'index'),
)