from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'ariadne'

urlpatterns = [
    path("", views.index, name="index"),
    path("solver", views.solver, name="solver"),
    path("solve_problem", views.solve_problem, name="solve_problem"),
    path("improved_index", views.improved_index, name="improved_index"),
    path("moon", views.moon, name="moon"),
    path("plane", views.plane, name="plane"),
    path("robots", views.robots, name="robots"),
]
