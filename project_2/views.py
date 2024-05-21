from django.http import HttpResponse

def contact(request):
    return HttpResponse("This is a contact Page.")

def home(request):
    return HttpResponse("This is a Home Page.")

def help(request):
    return HttpResponse("Welcome to help page And your request is accept.")