# myapp/views.py

from django.shortcuts import render
from django.utils.translation import gettext as _


def home(request):
    greeting = _("Hello, world!")
    return render(request, 'myapp/home.html', {'greeting': greeting})
