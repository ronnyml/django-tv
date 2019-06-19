# -*- encoding: utf-8 -*-

from rest_framework import routers
from django.urls import include, path
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'awards', views.AwardViewSet)
router.register(r'awards_categories', views.AwardCategoryViewSet)
router.register(r'cities', views.CityViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'festivals', views.FestivalViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'languages', views.LanguageViewSet)
router.register(r'movies_tvshows', views.MovieTVShowViewSet)
router.register(r'movies_tvshows_categories', views.MovieTVShowCategoryViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'people', views.PersonViewSet)
router.register(r'person_roles', views.PersonRoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]