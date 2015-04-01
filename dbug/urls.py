from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbug.views.home', name='home'),
    url(r'^snippet/', include('snippets.urls')),
    url(r'^fibonacci/', include('fibonacci.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
