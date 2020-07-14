import requests
import json

BASE = "http://127.0.0.1:8080/"

data = {"check": "secret"}

proxies = {
  "http": None,
  "https": None,
}

headers = {'Content-type':'application/json','Accept':'text/plain'}

response = requests.post(BASE + "api/scraping", data=data)

print(response.json())

