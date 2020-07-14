from rest_framework import serializers
from webscrape.models import Testing, rent

class TestingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testing
        fields = ('id',
                  'title',
                  'description',
                  'published')

class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = rent
        fields = ('id',
                  'links',
                  'names',
                  'addresses',
                  'states',
                  'prices',
                  'bedrooms',
                  'bathrooms',
                  'built_ups',
                  'built_years',
                  'house_types',
                  'furnishings',
                  'prices_per_sqft',
                  'images')
