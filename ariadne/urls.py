from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'ariadne'

urlpatterns = [
    path("", views.index, name="index"),
    path("solver", views.solver, name="solver"),
    path("solve_problem", views.solve_problem, name="solve_problem"),
]
