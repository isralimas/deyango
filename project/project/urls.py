# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^isra/([A-z]{4})/([A-z]{2})/$', 'app.views.current_datetime'),

    url(r'^([A-z]+)/(.+)/(.+)/$', 'app.views.suma', name='suma'),

    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^administrador/', include(admin.site.urls)),
)
