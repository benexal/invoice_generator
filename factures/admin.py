from django.contrib import admin
from .models import Facture, FactureProduit
# Register your models here.


class FactureProduitInline(admin.TabularInline):
    model = FactureProduit
    extra = 1  # Allows adding multiple products to a single invoice

class FactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date')
    search_fields = ('client__nom',)
    list_filter = ('date',)
    inlines = [FactureProduitInline]

admin.site.register(Facture, FactureAdmin)
admin.site.register(FactureProduit)