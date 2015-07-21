from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples: 
    url(r'^$', 'consulting.views.home', name='home'),
    url(r'^blog/','consulting.views.blog'),
    url(r'^about/$','consulting.views.about'),
    url(r'^contact/$','consulting.views.contact'),
    url(r'^admin/', include(admin.site.urls)),
)
