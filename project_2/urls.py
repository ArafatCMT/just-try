from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("help/", views.help),
    path("contact/", views.contact),
    path("test_app/", include("test_app.urls")),
    path("test_app_2/", include("test_app_2.urls"))
]
