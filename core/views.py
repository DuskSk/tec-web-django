from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Ola Mundo")


# Create your views here.
