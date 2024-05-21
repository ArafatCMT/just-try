from django.shortcuts import render
from django.http import HttpResponse

def emergency_help(requst):
    return HttpResponse("This is Emergency Help Page...")
