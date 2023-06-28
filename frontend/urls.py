from django.urls import path
from . import views

app_name = 'travelgpt'

urlpatterns = [
    path("", views.index, name="index"),
    path('itinerary_history/', views.itinerary_history, name='itinerary_history'),
    path("process_form/", views.process_form, name="process_form"),
    path("generated_itinerary/", views.generated_itinerary, name="generated_itinerary"),
    path("travel_plan/generated_itinerary/<int:itinerary_id>/", views.generated_itinerary, name="generated_itinerary"),
    path("beijing", views.beijing, name="beijing"),
    path("prague", views.prague, name="prague"),
    path("barcelona", views.barcelona, name="barcelona"),
]