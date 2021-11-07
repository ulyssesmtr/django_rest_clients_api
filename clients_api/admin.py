from django.contrib import admin
from clients_api.models import Client

class Clients (admin.ModelAdmin):
    list_display = ('id', 'nome')



admin.site.register(Client, Clients)
