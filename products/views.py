from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return HttpResponse('Products will be soon listed here')

def add(request):
    return HttpResponse('New product added')
