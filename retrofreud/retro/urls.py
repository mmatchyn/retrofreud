from django.conf.urls import patterns, url
from retro import views

urlpatterns = patterns('retro.views',
	url(r'^$', 'index'),
	url(r'^add/$', 'add', name='add_new_issue'),
	url(r'^sort/title/$', 'sort', {'sort_column':'title'}, name='sort_by_title'),
	url(r'^sort/date/$', 'sort', {'sort_column':'created'}, name='sort_by_created'),
	url(r'^sort/votes/$', 'sort', {'sort_column':'-votes'}, name='sort_by_votes'),
	url(r'^sort/state/$', 'sort', {'sort_column':'solved'}, name='sort_by_state'),
	url(r'^close/(?P<id>\d+)/$', 'close'),
	url(r'^open/(?P<id>\d+)/$', 'reopen'),
	url(r'^vote/(?P<id>\d+)/$', 'vote'),
	url(r'^update/(?P<id>\d+)/$', 'update'),
	url(r'^(?P<id>\d+)/$', 'issue'),
)
