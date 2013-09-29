# -*- coding: utf-8 -*-


from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{cookiecutter.project_name}}.views.home', name='home'),
    # url(r'^{{cookiecutter.project_name}}/', include('{{cookiecutter.project_name}}.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
