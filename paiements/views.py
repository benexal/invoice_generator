""" from django.shortcuts import render
import requests
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.

def proxy_to_kprimepay(request):
    url = "https://api-kprimepay.ro-cobra.net/v1/checkout"
    headers = {
        'Authorization': 'Bearer votre_sandbox_token',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=request.body, headers=headers)
    return JsonResponse(response.json())


@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        data = request.POST
        kpp_session_id = data.get('kpp_session_id')
        payment_status = data.get('payment_status')
        
        if payment_status == 'paid':
            # Traitez le paiement et générez la facture ici
            # Par exemple, enregistrez les informations dans la base de données
            return HttpResponse("Paiement validé et facture générée")
        else:
            # Traitez les cas où le paiement a échoué ou été rejeté
            return HttpResponse("Paiement échoué", status=400)
    return HttpResponse("Méthode non autorisée", status=405)
 """