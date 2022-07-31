from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Tales Silva'
    }, status=200)


def contato(request):
    return HttpResponse('CONTATO')


def sobre(request):
    return HttpResponse('SOBRE')
