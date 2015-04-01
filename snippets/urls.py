# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^all$', 'snippets.views.snippet_all', name="snippet_all"),
    url(r'^show/(?P<id>[0-9-]+)$', 'snippets.views.snippet_show', name="snippet_show"),
    url(r'^update/(?P<id>[0-9-]+)$', 'snippets.views.snippet_update', name="snippet_update"),
)


