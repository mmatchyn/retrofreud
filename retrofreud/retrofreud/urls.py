from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'retrofreud.views.home', name='home'),
    # url(r'^retrofreud/', include('retrofreud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'retrofreud.views.index'),
	url(r'^issues/', include('retro.urls')),
	url(r'^moodmeter/', include('moodmeter.urls')),
)
