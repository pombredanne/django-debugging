# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^(?P<num>[0-9-]+)$', 'fibonacci.views.fibonaci_view', name="fibonaci_view"),
)
