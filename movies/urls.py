# -*- encoding: utf-8 -*-

from django.conf.urls import url
from movies import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]