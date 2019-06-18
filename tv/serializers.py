from tv.models import MovieTVShow
from rest_framework import serializers

class MovieTVShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieTVShow
        fields = ('name', 'slug', 'trailer_url')