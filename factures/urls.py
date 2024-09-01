# factures/urls.py

from django.urls import path
from . import views  # Importer le module views

urlpatterns = [
    path('', views.index, name='index'),  # Associer la vue 'index' à la route racine ''
     path('list_invoice', views.listInvoice, name='list_invoice'),
    path('generate_invoice/', views.generate_invoice, name='generate_invoice'),
     path('factures/<int:facture_id>/pdf/', views.facture_pdf, name='facture_pdf'),
]
