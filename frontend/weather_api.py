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

def getWeatherForDays(location, start_date, end_date):

	location = urllib.parse.quote_plus(location)
	requestUrl = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/\
{location}/{start_date}/{end_date}?key={weather_api_key}"

	print(f"Weather requestUrl = {requestUrl}")

	try:
			req = urllib.request.urlopen(requestUrl)
	except:
			print(f"Could not read from: {requestUrl}")
			return []
		
	rawForecastData = req.read()
	req.close()
	days = json.loads(rawForecastData)['days']

	weather_string = ""
	for i, day in enumerate(days):
		temp = "moderate"
		if day['tempmax'] > 77:
			temp = "hot"
		elif day['tempmin'] < 50:
			temp = "cold"

		# cleaned up to give "temperature is hot/moderate/cold. + descriptionof day" -> feed to LLM
		weather_string += f"``day {i+1}: temperature is {temp}; {day['description']}`` \n"

	return weather_string