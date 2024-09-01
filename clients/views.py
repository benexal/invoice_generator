from django.shortcuts import render
from .models import Client
from django.http import JsonResponse
# Create your views here.

# clients/views.py

def get_clients(request):
    clients = Client.objects.all().values('id', 'nom', 'prenom')
    return JsonResponse({'clients': list(clients)})
