from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.test),
    path("about_us/", views.about_us),
    path("", views.home)
]