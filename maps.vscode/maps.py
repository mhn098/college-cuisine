import requests
import json
import warnings
import pandas as pd
import googlemaps
from googlemaps import convert
from googlemaps import convert
from datetime import datetime


def geocode(client):
    params = {}

    return client._request("/maps/api/geocode/json", params).get("results", [])


gmaps = googlemaps.Client(key='AIzaSyCF2eWrSk2vKk1UqHVpB_65fCSWMPIP7v0')

# Geocoding a random address
geocode_result = str(gmaps.geocode("213 W Franklin Street, Chapel Hill, NC"))
geocode_result = geocode_result.replace("\'", "\"")
geocode_info = json.loads(geocode_result)

geocode_lat = (geocode_info[0]['geometry']['location']['lat'])
geocode_lng = (geocode_info[0]['geometry']['location']['lng'])

#################

def places(client,query=None,location=None,radius=None,language=None,min_price=None,
    max_price=None,open_now=False,type=None,region=None,page_token=None,):

    return client._places(client,"text",query=query,location=location,radius=radius,language=language,
            min_price=min_price,max_price=max_price,open_now=open_now,type=type,region=region,
            page_token=page_token,
        )



url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=35.9114138%2C-79.05900489999999&radius=150&type=restaurant&key=AIzaSyCF2eWrSk2vKk1UqHVpB_65fCSWMPIP7v0"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

jason_response = json.loads(str(response.text))

#print(response.text)

for result in jason_response['results']:
    print(result['name'])



#retaurant_names = json.loads(response[])



#places_result = gmaps.places(location:("35.9114138", "-79.05900489999999"))

#print(places_result)
# dawg what is this returning and how do i even put in something into this