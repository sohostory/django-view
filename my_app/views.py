from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About Me Page")

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")

def add(request, num1, num2):
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")