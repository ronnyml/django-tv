from tv.models import *
from rest_framework import serializers


class AwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'

class AwardCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AwardCategory
        fields = '__all__'

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class FestivalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Festival
        fields = '__all__'

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class MovieTVShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieTVShow
        fields = '__all__'

class MovieTVShowCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieTVShowCategory
        fields = '__all__'

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PersonRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonRole
        fields = '__all__'
