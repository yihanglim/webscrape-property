from django.shortcuts import render
from webscrape.models import rent

# Create your views here.
def main(request):
    properties = rent.objects.order_by('id')
    return render(request, 'main.html', {'properties': properties})
