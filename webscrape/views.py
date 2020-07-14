from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from webscrape.models import Testing, rent
from webscrape.serializers import TestingSerializer, PropertySerializer
from rest_framework.decorators import api_view

from webscrape.scraping import scrape


@api_view(['GET','POST','DELETE'])
def property_list(request):
    if request.method == 'GET':
        properties = rent.objects.order_by('-pk')
        title = request.GET.get('title', None)
        if title is not None:
            properties = properties.filter(title__icontains=title)
        properties_serializer = PropertySerializer(properties, many=True)
        return JsonResponse(properties_serializer.data, safe=False)

    elif request.method == 'POST':
        property_data = JSONParser().parse(request)
        property_serializer = PropertySerializer(data=property_data, many=True)
        if property_serializer.is_valid():
            property_serializer.save()
            return JsonResponse({'message':'scraped successful'}, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse({'message':'scraped unsuccessful'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        properties = rent.objects.all()
        count = properties.delete()
        return JsonResponse({'message':'{} Property were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def property_detail(request,pk):
    try:
        property = rent.objects.get(pk=pk)
        if request.method == 'GET':
            properties_serializer = PropertySerializer(property)
            return JsonResponse(properties_serializer.data)
        elif request.method == 'PUT':
            property_data = JSONParser().parse(request)
            properties_serializer = PropertySerializer(property, data=property_data)
            if properties_serializer.is_valid():
                properties_serializer.save()
                return JsonResponse(properties_serializer.data)
            return JsonResponse(properties_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            property.delete()
            return JsonResponse({'message':'Property was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except rent.DoesNotExist:
        return JsonResponse({'message':'The property does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def start_scrape(request):
    if request.method == 'POST':
        #checking = JSONParser().parse(request)
        #check = checking['check']
        check = request.POST['check']
        if check == 'secret':
            property_data = scrape()
            property_serializer = PropertySerializer(data=property_data, many=True)
            if property_serializer.is_valid():
                property_serializer.save()
                return JsonResponse({'message': 'scraped successful'}, status=status.HTTP_201_CREATED, safe=False)
                #return JsonResponse(property_serializer.data, status=status.HTTP_201_CREATED, safe=False)
            return JsonResponse(property_serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
        else:
            return JsonResponse({'message':'unauthorised'}, status=status.HTTP_404_NOT_FOUND)


'''
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Testing.objects.filter(published=True)
    if request.method == 'GET':
        tutorials_serializer = TestingSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
'''
