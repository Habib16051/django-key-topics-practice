from django.shortcuts import render
from . forms import StudentRegistration
from django.http import HttpResponseRedirect
from . models import Student

# Create your views here.


def thanks(request):
    return render(request, 'success.html')


def show_data(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            # for adding element on the admin database
            # reg = Student(id=1, name=name, email=email, password=password)
            # reg.save()

            # for delete any element from the admin database
            reg = Student(id=1)
            reg.delete()

            return HttpResponseRedirect('/regi/')

    else:
        fm = StudentRegistration()
    return render(request, 'student.html', {'form': fm})
