""" from django.urls import path
from .views import proxy_to_kprimepay

urlpatterns = [
    # autres urls de votre projet
    path('kprimepay/proxy/', proxy_to_kprimepay, name='proxy_to_kprimepay'),
]   """