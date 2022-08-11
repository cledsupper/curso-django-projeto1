from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', {
        'name': 'Tales Silva'
    }, status=200)


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', {
        'name': 'Tales Silva'
    }, status=200)
