from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("You are at index page")

def add(request):
    return HttpResponse("You are at add page")

def delete(request):
    return HttpResponse("You are at delete page")