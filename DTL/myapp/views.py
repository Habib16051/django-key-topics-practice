from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name': 'Habib',
        'email': 'habibmhr143@gmail.com',
        'home': 'Brahmanbaria',
        'duration': "12-09-2020",
    }
    return render(request, 'home.html', context)
