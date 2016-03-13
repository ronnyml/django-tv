from django.conf.urls import patterns, include, url
from movies import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'movies.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
