# -*- encoding: utf-8 -*-

from django.urls import path
from tv import views

urlpatterns = [
    path('', views.index, name='index'),
]