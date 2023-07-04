import urllib.parse
import urllib.request
import json
import time
import matplotlib.pyplot as plt
import pandas as pd
import pdb
import os

# Key features to implement - using VisualCrossing API (as the first API to try)

# If any of the days are within the next 14 days, notify the user that weather planning will be used to optimise the trip plan.
# This will be done by targeting the date fields in the frontend (if possible)

# Prompt engineered features
# Plan activities around sun, rain, etc
# If too hot (30+), don't spend mid-day outside / organise in a refreshing drink/sit down
# If too cold (below 10), organise warm drinks and warming activities
# If raining, try to move indoor activities to this day, and perform less outdoor activities

# Hard-coded features
# Recommend daily clothing based on weather - rain=raincoat+umbrella, sun=suncream, wind=coat
# Recommend clothing to pack based on the temperature and rain probabilities

weather_api_key = os.environ.get('WEATHER_API_KEY')
location = "New York City, NY" # City, state/province is most accurate. Get LLM to feed this in (city dropdown is best)
unit_group="us"

def getWeatherForecast(api_key, location, unit_group):
         requestUrl = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + urllib.parse.quote_plus(location)
         requestUrl = requestUrl+"?key="+api_key+"&unitGroup="+unit_group+"&include=days"

         print(f"Weather requestUrl = {requestUrl}")

         try:
                 req = urllib.request.urlopen(requestUrl)
         except:
                 print(f"Could not read from: {requestUrl}")
                 return []
                
         rawForecastData = req.read()
         req.close()
         return json.loads(rawForecastData)
    
weatherForecast = getWeatherForecast(weather_api_key, location, unit_group)

print(f"Weather forecast for {weatherForecast['resolvedAddress']}")
days = weatherForecast['days']

# pdb.set_trace()

for day in days:
    # if day['tempmax'] > 
    print(f"{day['datetime']} - Temp: {day['tempmax']}F - {day['tempmin']}F. \"{day['description']}\"")

    # clean up to give "temperature is hot/moderate/cold. + description" -> feed to LLM