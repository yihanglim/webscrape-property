from bs4 import BeautifulSoup
from requests import get
import requests

import time
from random import randint


def scrape():
    links = []
    names = []
    addresses = []
    states = []
    prices = []
    bedrooms = []
    bathrooms = []
    built_ups = []
    built_years = []
    house_types = []
    furnishings = []
    prices_per_sqft = []
    images = []

    n_pages = 0
    #headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    headers = ({'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'})

    for page in range(1, 100):
        url = "https://www.propertyguru.com.my/property-for-rent" + "/" + str(page)
        r = get(url, headers=headers)
        page = BeautifulSoup(r.text, 'html.parser')
        house_containers = page.find_all('div', class_="listing-card")
        if house_containers != []:
            n_pages += 1
            for house in house_containers:
                link = house.find_all('a')[3].get('href')
                print(link)
                links.append(link)

                name = house.find_all('a')[3].text
                print(name)
                names.append(name)

                address = house.find_all('p', class_="listing-location ellipsis")[0].text
                address = address.replace('- ', '')
                print(address)
                addresses.append(address)

                state = address[::-1].split(" ,")[0][::-1]
                print(state)
                states.append(state)

                price = house.find_all('span', class_="price")[0].text
                price = int(price.replace(',', ''))
                print(price)
                prices.append(price)

                bedroom = house.find_all('li', class_="listing-rooms pull-left")[0].find_all('span')[0].text.strip()
                print(bedroom)
                bedrooms.append(bedroom)

                try:
                    bathroom = house.find_all('li', class_="listing-rooms pull-left")[0].find_all('span')[1].text.strip()
                    print(bathroom)
                    bathrooms.append(bathroom)
                except:
                    bathrooms.append("N.A")

                built_up = house.find_all('li', class_="listing-floorarea pull-left")[0].text
                built_up = int(built_up.split('sqft')[0].strip())
                print(built_up)
                built_ups.append(built_up)

                try:
                    built_year = house.find_all('ul', class_="clear-both listing-property-type")[0].find_all('li',class_="pull-left new-launch")[0].text
                    built_year = built_year[12:]
                    print(built_year)
                    built_years.append(built_year)

                    house_type = house.find_all('ul', class_="clear-both listing-property-type")[0].find_all('li', class_="pull-left")[1].text
                    print(house_type)
                    house_types.append(house_type)

                    try:
                        furnishing = house.find_all('ul', class_="clear-both listing-property-type")[0].find_all('li',
                                                                                                                 class_="pull-left")[
                            2].text
                        print(furnishing)
                        furnishings.append(furnishing)

                    except:
                        furnishings.append("N.A")
                except:
                    house_type = house.find_all('ul', class_="clear-both listing-property-type")[0].find_all('li', class_="pull-left")[0].text
                    print(house_type)
                    house_types.append(house_type)
                    try:
                        temp = house.find_all('ul', class_="clear-both listing-property-type")[0].find_all('li',class_="pull-left")[1].text

                        if list(temp)[0] == "B":
                            built_year = temp[7:]
                            print(built_year)
                            built_years.append(built_year)
                            furnishings.append("N.A")
                        else:
                            furnishing = temp
                            print(furnishing)
                            furnishings.append(furnishing)
                            try:
                                built_year = house.find_all('ul', class_="clear-both listing-property-type")[0].find_all('li',class_="pull-left")[2].text
                                built_year = built_year[7:]
                                print(built_year)
                                built_years.append(built_year)
                            except:
                                built_years.append("N.A")
                    except:
                        built_years.append("N.A")
                        furnishings.append("N.A")
                try:
                    price_per_sqft = house.find_all('li', class_="listing-floorarea pull-left")[1].text[3:7]
                    price_per_sqft = float(price_per_sqft)
                    print(price_per_sqft)
                    prices_per_sqft.append(price_per_sqft)
                except:
                    prices_per_sqft.append('N.A')

                image = house.find_all('div', class_="gallery-wrapper")[0].get("data-gallery")
                image = image.split(':"')[1].split('"},')[0].replace('\\', '')
                print(image)
                images.append(image)

        else:
            #return links, names, addresses, states, prices, bedrooms, bathrooms, built_ups, built_years, house_types, furnishings, prices_per_sqft, images
            all_property = [{'links': links1,
                    'names': names1,
                    'addresses': addresses1,
                    'states': states1,
                    'prices': prices1,
                    'bedrooms': bedrooms1,
                    'bathrooms': bathrooms1,
                    'built_ups': built_ups1,
                    'built_years': built_years1,
                    'house_types': house_types1,
                    'furnishings': furnishings1,
                    'prices_per_sqft': prices_per_sqft1,
                    'images': images1}
                   for
                   links1, names1, addresses1, states1, prices1, bedrooms1, bathrooms1, built_ups1, built_years1, house_types1, furnishings1, prices_per_sqft1, images1
                   in zip(links, names, addresses, states, prices, bedrooms, bathrooms, built_ups, built_years,
                          house_types, furnishings, prices_per_sqft, images)]

            #response = requests.post(BASE + "api/scraping", json=all_property, headers=headers)
            #print(response.json())
            return all_property

        time.sleep(randint(5, 10))

    all_property = [{'links':links1,
            'names':names1,
            'addresses':addresses1,
            'states':states1,
            'prices':prices1,
            'bedrooms':bedrooms1,
            'bathrooms':bathrooms1,
            'built_ups':built_ups1,
            'built_years':built_years1,
            'house_types':house_types1,
            'furnishings':furnishings1,
            'prices_per_sqft':prices_per_sqft1,
            'images':images1}
           for links1, names1, addresses1, states1, prices1, bedrooms1, bathrooms1, built_ups1, built_years1, house_types1, furnishings1, prices_per_sqft1, images1
           in zip(links, names, addresses, states, prices, bedrooms, bathrooms, built_ups, built_years, house_types, furnishings, prices_per_sqft, images)]

    return all_property



