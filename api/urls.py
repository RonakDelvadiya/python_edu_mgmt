from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from education_mgmt import settings

from .views import *
from rest_framework.authtoken import views as tokenView

urlpatterns = patterns('',
    url(r'^register/$',user_create),
    url(r'^login/',tokenView.obtain_auth_token),
    url(r'^university/list/$', university_list),
    url(r'^school/add/$', school_create),
    url(r'^school/list/$', school_list),
    url(r'^school/details/(?P<pk>[0-9]+)/$', school_details),
    url(r'^school/update/(?P<pk>[0-9]+)/$', school_update),
    url(r'^school/delete/(?P<pk>[0-9]+)/$', school_delete),
    url(r'^universitylistschool/$', university_list2),
    url(r'^studentcreate/$', student_create),
    url(r'^university/delete/(?P<pk>[0-9]+)/$', university_delete),

)
