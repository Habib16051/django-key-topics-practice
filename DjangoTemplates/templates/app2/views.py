from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def brahmanbaria(request):
    return render(request, 'courseone.html')


def rangpur(request):
    return render(request, 'coursetwo.html')
