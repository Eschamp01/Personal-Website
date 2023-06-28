from django.shortcuts import render

def index(request):
    return render(request, 'homepage/index.html')

def new_index(request):
    return render(request, 'homepage/new_index.html')