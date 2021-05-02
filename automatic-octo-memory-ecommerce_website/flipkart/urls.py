from django.contrib import admin
from django.urls import path
from .views import Well, Smartphone

urlpatterns = [
    path('', Well, name = 'Home'),
    path('phone/', Smartphone, name = 'phone')

]
        