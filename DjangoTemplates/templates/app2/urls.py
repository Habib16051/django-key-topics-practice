from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('b/', views.brahmanbaria),
    path('r/', views.rangpur),

]
