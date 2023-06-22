from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'homepage'

urlpatterns = [
    path("", views.index, name="index"),
]
