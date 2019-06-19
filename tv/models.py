# -*- coding: utf-8 -*-

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify

MAX_LENGTH = 255

class Genre(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    
    class Meta:
        db_table = 'tv_genres'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

class Country(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    code = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'tv_countries'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

class City(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tv_cities'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)
               
class Organization(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    abbreviation = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    website = models.URLField(max_length=MAX_LENGTH, blank=True)
    creation_date = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'tv_organizations'
        verbose_name_plural = 'Award Organizations'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Organization, self).save(*args, **kwargs)    

class AwardCategory(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    awarded_for = models.CharField(max_length=MAX_LENGTH)
    creation_year = models.PositiveSmallIntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'tv_award_categories'
        verbose_name_plural = 'Award Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(AwardCategory, self).save(*args, **kwargs)

class Award(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    description = models.TextField(max_length=MAX_LENGTH, blank=True)
    presented_by = models.ForeignKey(Organization, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    creation_date = models.DateField(null=True, blank=True)
    website = models.URLField(max_length=MAX_LENGTH, blank=True)
    category = models.ManyToManyField(AwardCategory)
    
    class Meta:
        db_table = 'tv_awards'
        verbose_name_plural = 'Awards'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Award, self).save(*args, **kwargs)

class Festival(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    description = models.TextField(max_length=MAX_LENGTH, blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    founded = models.DateField(blank=True)
    website = models.URLField(max_length=MAX_LENGTH, blank=True)
    
    class Meta:
        db_table = 'tv_festivals'
        verbose_name_plural = 'Festivals'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Festival, self).save(*args, **kwargs)

class Language(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    code = models.CharField(max_length=5)
    
    class Meta:
        db_table = 'tv_languages'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Language, self).save(*args, **kwargs)       

class PersonRole(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    
    class Meta:
        db_table = 'tv_person_roles'
        verbose_name_plural = 'Person Roles'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PersonRole, self).save(*args, **kwargs)

class Person(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    birth_date = models.DateField(blank=True)
    person_role = models.ManyToManyField(PersonRole)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/people/', blank=True)
     
    class Meta:
        db_table = 'tv_people'
        verbose_name_plural = 'People'

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name
      
    def full_name(self):
       full_name = self.first_name + ' ' + self.last_name
       return full_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name) + '-' + slugify(self.last_name)
        super(Person, self).save(*args, **kwargs)

class MovieTVShowCategory(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    
    class Meta:
        db_table = 'tv_movies_tvshows_categories'
        verbose_name_plural = 'Movie TV Shows Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MovieTVShowCategory, self).save(*args, **kwargs)

class MovieTVShow(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    name_es = models.CharField(max_length=MAX_LENGTH,
                               verbose_name='Spanish Latin America', blank=True)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    category = models.ForeignKey(MovieTVShowCategory, on_delete=models.PROTECT)
    description = models.TextField(max_length=MAX_LENGTH, blank=True)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey(Person, on_delete=models.PROTECT)
    release_date = models.DateField(blank=True)
    budget = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=12)
    running_time = models.CharField(max_length=10, null=True, blank=True)
    country = models.ManyToManyField(Country)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    website = models.URLField(max_length=MAX_LENGTH, blank=True)
    trailer_url = models.URLField(max_length=MAX_LENGTH, blank=True)
    no_seasons = models.PositiveSmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/movie_tvshows/', blank=True)
    award_category = models.ManyToManyField(AwardCategory, blank=True)
    festival = models.ManyToManyField(Festival, blank=True)
    
    class Meta:
        db_table = 'tv_movies_tvshows'
        verbose_name_plural = 'Movies TV Shows'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MovieTVShow, self).save(*args, **kwargs)