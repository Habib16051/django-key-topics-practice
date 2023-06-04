
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_data, name='student'),
    path('regi/', views.thanks, name='regi'),

]
