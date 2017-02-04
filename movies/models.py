# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from utils.image_thumbs import ImageWithThumbsField

MAX_LENGTH = 255

class Genre(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    
    class Meta:
        db_table = 'movies_genres'
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
        db_table = 'movies_countries'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

class City(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    country = models.ForeignKey(Country)
    
    class Meta:
        db_table = 'movies_cities'
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
    country = models.ForeignKey(Country)
    formation = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'movies_organizations'
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Organization, self).save(*args, **kwargs)         

class AwardCategory(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    awarded_for = models.CharField(max_length=MAX_LENGTH)
    first_awarded = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'movies_award_categories'
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
    presented_by = models.ForeignKey(Organization)
    country = models.ForeignKey(Country)
    formation = models.PositiveIntegerField()
    website = models.URLField(max_length=MAX_LENGTH, blank=True)
    category = models.ManyToManyField(AwardCategory)
    
    class Meta:
        db_table = 'movies_awards'
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
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    founded = models.DateField(blank=True)
    website = models.URLField(max_length=MAX_LENGTH, blank=True)
    
    class Meta:
        db_table = 'movies_festivals'
        verbose_name_plural = 'Festivals'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Festival, self).save(*args, **kwargs)

class Language(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    code = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'movies_languages'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Language, self).save(*args, **kwargs)       

class PersonType(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    
    class Meta:
        db_table = 'movies_person_types'
        verbose_name_plural = 'Person Types'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PersonType, self).save(*args, **kwargs)

class Person(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    birth_date = models.DateField(blank=True)
    person_type = models.ManyToManyField(PersonType)
    country = models.ForeignKey(Country)
    image = ImageWithThumbsField(upload_to='images/people/', blank=True, 
                                 sizes=((100, 100), (200, 200)))
     
    class Meta:
        db_table = 'movies_people'
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

class Movie(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    name_es = models.CharField(max_length=MAX_LENGTH,
                               verbose_name='Spanish Latin America')
    slug = models.SlugField(max_length=MAX_LENGTH, blank=True)
    description = models.TextField(max_length=MAX_LENGTH, blank=True)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey(Person)
    release_date = models.DateField(blank=True)
    budget = models.DecimalField(blank=True, decimal_places=2, max_digits=12)
    running_time = models.PositiveIntegerField(blank=True)
    country = models.ManyToManyField(Country)
    language = models.ForeignKey(Language)
    website = models.URLField(max_length=MAX_LENGTH, blank=True)
    trailer_url = models.URLField(max_length=MAX_LENGTH, blank=True)
    image = ImageWithThumbsField(upload_to='images/movies/', blank=True, 
                                 sizes=((100, 100), (200, 200)))
    award_category = models.ManyToManyField(AwardCategory, blank=True)
    festival = models.ManyToManyField(Festival, blank=True)
    
    class Meta:
        db_table = 'movies_movies'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)