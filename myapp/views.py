from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(request,"<h1>welcome my world</h1>")
def child(request):
    return render(request,"child.html")
def home(request):
    return render(request,"myapp1/home.html",{'name':"Akhil"})
