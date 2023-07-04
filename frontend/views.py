from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import openai_api
import json
import pdb
from . import weather_api
import os

weather_api_key = os.environ.get('WEATHER_API_KEY')

def index(request):
    return render(request, 'frontend/index.html')

def itinerary_history(request):
    return render(request, 'frontend/itinerary_history.html')

def process_form(request):
    if request.method == "POST":
        travel_params_dict = {
            'destination': request.POST.get('destination'),
            'arrival_date': request.POST.get('arrival-date'),
            'arrival_time': request.POST.get('arrival-time'),
            'departure_date': request.POST.get('departure-date'),
            'departure_time': request.POST.get('departure-time'),
            'num_travellers': request.POST.get('num-travellers'),
            'interests': request.POST.getlist('interests'),
            'trip_intensity': request.POST.get('trip-intensity'),
            'physical_activity_level': request.POST.get('activity-level'),
            'timing_preciseness': request.POST.get('timing-preciseness'),
            'relaxed_first_day' : request.POST.get('relaxed-first-day'),
        }
        
        weather_string = weather_api.getWeatherForDays(weather_api_key, travel_params_dict['destination'], \
                                            travel_params_dict['arrival_date'], travel_params_dict['departure_date'])
        travel_params_dict['weather_string'] = weather_string

        itinerary = openai_api.create_travel_itinerary(travel_params_dict)
        result = {'itinerary': itinerary}
        return JsonResponse(result)

    return HttpResponse("The reauest was meant to be a POST request, but this one was not.")


def generated_itinerary(request):
    itinerary = request.GET.get('itinerary')
    return render(request, 'frontend/generated_itinerary.html', {'itinerary': itinerary})

def beijing(request):
    return render(request, 'frontend/beijing.html')

def prague(request):
    return render(request, 'frontend/prague.html')

def barcelona(request):
    return render(request, 'frontend/barcelona.html')