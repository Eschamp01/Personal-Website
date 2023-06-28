from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'homepage'

urlpatterns = [
    path("", views.new_index, name="new_index"),
    path("old", views.index, name="index"),
]
