from django.contrib import admin
from clients_api.models import Cliente

class Clientes (admin.ModelAdmin):
    list_display = ('id', 'nome')



admin.site.register(Cliente, Clientes)
