# clients/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('get-clients/', views.get_clients, name='get_clients'),
]
