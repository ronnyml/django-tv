# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import viewsets
from tv.models import MovieTVShow
from tv.serializers import MovieTVShowSerializer

class MovieTVShowViewSet(viewsets.ModelViewSet):
    queryset = MovieTVShow.objects.all()
    serializer_class = MovieTVShowSerializer
    
def index(request):
    return render(request, 'index.html', {})
    