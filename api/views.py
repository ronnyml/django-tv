from rest_framework import viewsets
from tv.models import MovieTVShow
from .serializers import *


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all().order_by('name')
    serializer_class = AwardSerializer

class AwardCategoryViewSet(viewsets.ModelViewSet):
    queryset = AwardCategory.objects.all().order_by('name')
    serializer_class = AwardCategorySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer

class FestivalViewSet(viewsets.ModelViewSet):
    queryset = Festival.objects.all().order_by('name')
    serializer_class = FestivalSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('name')
    serializer_class = LanguageSerializer

class MovieTVShowViewSet(viewsets.ModelViewSet):
    queryset = MovieTVShow.objects.all().order_by('name')
    serializer_class = MovieTVShowSerializer

class MovieTVShowCategoryViewSet(viewsets.ModelViewSet):
    queryset = MovieTVShowCategory.objects.all().order_by('name')
    serializer_class = MovieTVShowCategorySerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('name')
    serializer_class = OrganizationSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('first_name')
    serializer_class = PersonSerializer

class PersonRoleViewSet(viewsets.ModelViewSet):
    queryset = PersonRole.objects.all().order_by('name')
    serializer_class = PersonRoleSerializer
