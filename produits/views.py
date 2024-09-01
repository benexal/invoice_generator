from django.shortcuts import render
from django.http import JsonResponse
from .models import Categorie, Produit



# Create your views here.
""" def get_products(request):
    category_id = request.GET.get('category_id')
    if category_id:
        produits = Produit.objects.filter(categorie_id=category_id)
        produits_data = [{'id': produit.id, 'nom': produit.nom} for produit in produits]
        return JsonResponse({'produits': produits_data})
    return JsonResponse({'produits': []}) """


def get_categories(request):
    categories = Categorie.objects.all().values('id', 'nom')
    return JsonResponse({'categories': list(categories)})

def get_products_by_category(request):
    category_id = request.GET.get('category_id')
    produits = Produit.objects.filter(categorie_id=category_id).values('id', 'nom', 'prix', 'tva')
    return JsonResponse({'produits': list(produits)})
