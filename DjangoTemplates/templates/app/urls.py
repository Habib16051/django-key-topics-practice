from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dj/', views.learn_django),
    path('py/', views.learn_python),

]