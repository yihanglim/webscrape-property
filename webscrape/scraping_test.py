import requests
from rest_framework.response import Response
from django.http.response import JsonResponse
import csv

def scrape():
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    BASE = "http://127.0.0.1:8080/"

    data = [{'links': 'https://www.propertyguru.com.my/property-listing/shamelin-star-for-rent-by-david-cho-31309800',
      'names': 'Shamelin Star', 'addresses': 'Shamelin Star Jalan 4/91, Taman Shamelin Perkasa, Cheras, Kuala Lumpur',
      'states': 'Kuala Lumpur', 'prices': 2600, 'bedrooms': 3, 'bathrooms': 2, 'built_ups': 974, 'built_years': 2016,
      'house_types': 'Service Residence', 'furnishings': 'Fully Furnished', 'prices_per_sqft': 2.67,
      'images': 'https://my2-cdn.pgimgs.com/listing/31309800/UPHO.149036349.R400X300/Shamelin-Star-Cheras-Malaysia.jpg'},
     {
         'links': 'https://www.propertyguru.com.my/property-listing/the-grand-subang-ss13-for-rent-by-laraine-chong-31282316',
         'names': 'The Grand Subang SS13',
         'addresses': '7-5, Jalan SS 13/4, Subang Jaya Industrial Estate, Subang Jaya, Selangor', 'states': 'Selangor',
         'prices': 1900, 'bedrooms': 2, 'bathrooms': 2, 'built_ups': 550, 'built_years': 2019,
         'house_types': 'Service Residence', 'furnishings': 'Fully Furnished', 'prices_per_sqft': 1.25,
         'images': 'https://my2-cdn.pgimgs.com/listing/31282316/UPHO.148792961.R400X300/The-Grand-Subang-SS13-Subang-Jaya-Malaysia.jpg'
     }]

    data2 = [{'links': 'https://www.propertyguru.com.my/property-listing/andaman-quayside-for-rent-by-dominic-ong-22406786',
              'names': 'Andaman @ Quayside',
              'addresses': 'Quayside Off Jalan Seri Tanjung Pinang, Seri Tanjung Pinang, Tanjung Tokong, Timor Laut (Island), Penang', 'states': 'Penang', 'prices': 7200, 'bedrooms': '3', 'bathrooms': '4', 'built_ups': 2770, 'built_years': '2013',
            'house_types': 'Condominium', 'furnishings': 'Fully Furnished', 'prices_per_sqft': 2.6,
              'images': 'https://my2-cdn.pgimgs.com/listing/22406786/UPHO.144162271.R400X300/Andaman-Quayside-Timor-Laut-Island-Malaysia.jpg'},
             {'links': 'https://www.propertyguru.com.my/property-listing/sky-suites-klcc-for-rent-by-cannis-choy-30040236', 'names': 'Sky Suites @ KLCC', 'addresses': '56-1Residensi Sultan Ismail, Jalan Sultan Ismail, KL City, Kuala Lumpur', 'states': 'Kuala Lumpur', 'prices': 3000, 'bedrooms': '2', 'bathrooms': '2', 'built_ups': 649, 'built_years': ' 2019',
            'house_types': 'Apartment', 'furnishings': 'Fully Furnished', 'prices_per_sqft': 4.62,
              'images': 'https://my1-cdn.pgimgs.com/listing/30040236/UPHO.137891462.R400X300/Sky-Suites-KLCC-KL-City-Malaysia.jpg'}, {'links': 'https://www.propertyguru.com.my/property-listing/skyluxe-on-the-park-bukit-jalil-for-rent-by-kiru-kok-30763558',
            'names': 'Skyluxe On The Park @ Bukit Jalil', 'addresses': 'Jalan Jalil Perkasa 4, Bukit Jalil, Kuala Lumpur', 'states': 'Kuala Lumpur', 'prices': 1850, 'bedrooms': '2', 'bathrooms': '1', 'built_ups': 727, 'built_years': ' 2020',
            'house_types': 'Service Residence', 'furnishings': 'Partially Furnished', 'prices_per_sqft': 2.54,
            'images': 'https://my1-cdn.pgimgs.com/listing/30763558/UPHO.148298152.R400X300/Skyluxe-On-The-Park-Bukit-Jalil-Bukit-Jalil-Malaysia.jpg'}]


    print("data accessed")
    #response = requests.post(BASE + "api/property", json=data, headers=headers)
    #print(response.json())

    keys = ['links', 'names', 'addresses', 'states', 'prices', 'bedrooms', 'bathrooms', 'built_ups', 'built_years',
            'house_types', 'furnishings', 'prices_per_sqft', 'images']
    with open('../frontend/static/property_data2.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

    return data

response = scrape()
print(response)
