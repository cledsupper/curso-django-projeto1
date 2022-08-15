from django.shortcuts import get_list_or_404, render

from recipes.models import Recipe

# from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', {
        'title': 'Home',
        'recipes': recipes,
    }, status=200)


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #    category__id=category_id,
    #    is_published=True
    # ).order_by('-id')

    # recipes = get_list_or_404(
    #    Recipe,
    #    category__id=category_id, is_published=True
    # )

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/home.html', {
        'title': f'{recipes[0].category.name} - Category',
        'recipes': recipes,
    }, status=200)


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', {
        'title': f'{recipe.title} - Recipe',
        'recipe': recipe,
        'is_detail_page': True,
    }, status=200)
