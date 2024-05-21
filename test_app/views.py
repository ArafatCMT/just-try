from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Welcome to test Page..!")

def about_us(request):
    return HttpResponse("Welcome to our About Page.!")

def home(request):
    return HttpResponse("This is test home Page....!!")
