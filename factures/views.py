
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import json
from .models import Facture, FactureProduit
from clients.models import Client
from produits.models import Produit
import logging
from django.shortcuts import render
from weasyprint import HTML
from django.urls import reverse
import logging
from django.http import FileResponse
from django.conf import settings
import os


# Configurer le logger
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'factures/create_invoice.html')


""" def listInvoice(request):
    return render(request, 'factures/list_invoice.html') """



def listInvoice(request):
    factures = Facture.objects.all().select_related('client')
    context = {
        'factures': factures
    }
    return render(request, 'factures/list_invoice.html', context)


@csrf_exempt
def generate_invoice(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.debug(f'Données reçues: {data}')

            # Récupérer les données de la facture
            client_id = data['client']
            items = data['items']
            total_ht = 0  # Total hors taxes

            # Récupérer le client
            client = Client.objects.get(id=client_id)
            logger.debug(f'Client trouvé: {client}')

            # Créer une nouvelle facture
            facture = Facture(client=client)
            facture.save()
            logger.debug(f'Facture créée: {facture}')

            # Ajouter les produits à la facture
            for item in items:
                logger.debug(f'Ajout de l\'article: {item}')
                produit = Produit.objects.get(id=item['produit_id'])
                quantite = item['quantite']
                prix_unitaire = item['prix_unitaire']

                montant_ht = quantite * prix_unitaire
                tva = produit.tva  # Pourcentage de TVA du produit
                montant_tva = montant_ht * (tva / 100)
                montant_ttc = montant_ht + montant_tva

                # Ajouter le produit à la facture
                facture_produit = FactureProduit(
                    facture=facture,
                    produit=produit,
                    quantite=quantite,
                    prix_unitaire=prix_unitaire
                )
                facture_produit.save()
                logger.debug(f'Produit ajouté à la facture: {facture_produit}')

                total_ht += montant_ht

            total_tva = total_ht * (produit.tva / 100)
            total_ttc = total_ht + total_tva

            # Générer le PDF de la facture
            html_content = render_to_string('factures/invoice.html', {
                'facture': facture,
                'client': client,
                'items': FactureProduit.objects.filter(facture=facture),  # Liste des produits liés à la facture
                'total_ht': total_ht,
                'total_tva': total_tva,
                'total_ttc': total_ttc
            })
            pdf_file = HTML(string=html_content).write_pdf()

            # Définir le chemin du répertoire
            pdf_dir = os.path.join('media', 'factures')
            # Vérifier si le répertoire existe, sinon le créer
            if not os.path.exists(pdf_dir):
                os.makedirs(pdf_dir)

            # Enregistrer le fichier PDF
            pdf_path = os.path.join(pdf_dir, f'facture_{facture.id}.pdf')
            with open(pdf_path, 'wb') as f:
                f.write(pdf_file)

            # Retourner l'URL du fichier PDF
            pdf_url = reverse('facture_pdf', args=[facture.id])
            return JsonResponse({'pdf_url': pdf_url, 'facture_id': facture.id})

        except Client.DoesNotExist:
            logger.error('Client non trouvé')
            return JsonResponse({'error': 'Client non trouvé'}, status=404)
        except Produit.DoesNotExist:
            logger.error('Produit non trouvé')
            return JsonResponse({'error': 'Produit non trouvé'}, status=404)
        except Exception as e:
            logger.error(f'Erreur: {str(e)}')
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)



def facture_pdf(request, facture_id):
    # Construire le chemin du fichier PDF
    pdf_path = os.path.join(settings.MEDIA_ROOT, f'factures/facture_{facture_id}.pdf')

    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        return JsonResponse({'error': 'Fichier PDF non trouvé'}, status=404)


