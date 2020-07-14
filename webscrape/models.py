from django.db import models

class Testing(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)

class rent(models.Model):
    links = models.CharField(max_length=200, blank=False, default='')
    names = models.CharField(max_length=200, blank=False, default='')
    addresses = models.CharField(max_length=200, blank=False, default='')
    states = models.CharField(max_length=70, blank=False, default='')
    prices = models.IntegerField()
    bedrooms = models.CharField(max_length=50, blank=False, default='')
    bathrooms = models.CharField(max_length=50, blank=False, default='')
    built_ups = models.IntegerField()
    built_years = models.CharField(max_length=50, blank=False, default='')
    house_types = models.CharField(max_length=70, blank=False, default='')
    furnishings = models.CharField(max_length=70, blank=False, default='')
    prices_per_sqft = models.CharField(max_length=50, blank=False, default='')
    images = models.CharField(max_length=200, blank=False, default='')








