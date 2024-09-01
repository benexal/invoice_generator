# urls.py (dans votre application 'produits')
from django.urls import path
from .views import get_categories, get_products_by_category

urlpatterns = [
    path('get-categories/', get_categories, name='get_categories'),
    path('get-products-by-category/', get_products_by_category, name='get_products_by_category'),
]
