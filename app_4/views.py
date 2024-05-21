from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myApp(request):
    return HttpResponse("welCome to MyApps...")
