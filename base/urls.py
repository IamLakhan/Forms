from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('forms/', form_general),
]