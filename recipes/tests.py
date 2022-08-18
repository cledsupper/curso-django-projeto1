from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={"category_id": 123})
        self.assertEqual(url, '/recipes/category/123/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 123})
        self.assertEqual(url, '/recipes/123/')
