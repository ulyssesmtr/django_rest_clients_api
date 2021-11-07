from django.shortcuts import render
from rest_framework import  viewsets, generics
from clients_api.models import Client
from clients_api.serializer import ClienteSerializer, ClienteSerializerV2

from rest_framework import filters

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ClienteSerializerV2
        else:
            return ClienteSerializer

    http_method_names = ['get', 'post']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']
    ordering_fields = ['data_nascimento']
    
class ClientesPorSexo(generics.ListAPIView):
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ClienteSerializerV2
        else:
            return ClienteSerializer
  
    def get_queryset(self):
        sex = self.kwargs['gender']
        queryset = Client.objects.filter(sexo=sex)
        return queryset
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']
    ordering_fields = ['data_nascimento']

class ClientesPorEstado(generics.ListAPIView):
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ClienteSerializerV2
        else:
            return ClienteSerializer

    def get_queryset(self):
        state = self.kwargs['state']
        queryset = Client.objects.filter(estado=state)
        return queryset

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']
    ordering_fields = ['data_nascimento']

class ClientesPorCpf(generics.ListAPIView):
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ClienteSerializerV2
        else:
            return ClienteSerializer

    def get_queryset(self):
        cpf = self.kwargs['cpf']
        queryset = Client.objects.filter(cpf=cpf)
        return queryset

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']
    ordering_fields = ['data_nascimento']