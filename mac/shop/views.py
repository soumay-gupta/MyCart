from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'shop/index.html')


def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("in contact")

def tracker(request):
    return HttpResponse("in tracker")

def search(request):
    return HttpResponse("in search")

def productView(request):
    return HttpResponse("in product View")

def checkout(request):
    return HttpResponse("in checkout")