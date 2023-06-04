from django.shortcuts import render
from . forms import StudentRegistration
from django.http import HttpResponseRedirect

# Create your views here.


def thanks(request):
    return render(request, 'success.html')


def show_data(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Name :', fm.cleaned_data['name'])
            print('Email :', fm.cleaned_data['email'])
            # print('Password :', fm.cleaned_data['password'])
            # print('Agree :', fm.cleaned_data['agree'])

            return HttpResponseRedirect('/regi/')

    else:
        fm = StudentRegistration()
    return render(request, 'student.html', {'form': fm})
