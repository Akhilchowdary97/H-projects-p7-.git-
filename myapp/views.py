from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(request,"<h1>welcome my world</h1>")
