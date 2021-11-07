from rest_framework import serializers
from clients_api.models import Client
from clients_api.validator import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'estado', 'sexo']

    def validate(self, data):
    
        if not valid_name(data['nome']):
            raise serializers.ValidationError({'nome': 'The name cannot contain numbers'})

        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'Invalid CPF. Should have 11 digits and no dots . or -'})
        
        if not valid_date(data['data_nascimento']):
            raise serializers.ValidationError({'data_nascimento':'Date should be a previous date from the date of creation.'})
        
        if not valid_state(data['estado']):
            raise serializers.ValidationError({'estado':'Should be one in the state list'})
        
        if not valid_sex(data['sexo']):
            raise serializers.ValidationError({'sexo':'Should be either M or F'})

        return data
        
class ClienteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','nome', 'rg', 'cpf', 'data_nascimento', 'numero_celular', 'estado', 'sexo']

    def validate(self, data):
    
        if not valid_name(data['nome']):
            raise serializers.ValidationError({'nome': 'The name cannot contain numbers'})

        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'Invalid CPF. Must have 11 digits and no dots . or -'})

        if not valid_rg(data['rg']):
            raise serializers.ValidationError({'rg':'Invalid RG, must have 9 digits.'})
        
        if not valid_date(data['data_nascimento']):
            raise serializers.ValidationError({'data_nascimento':'Date should be a previous date from the date of creation.'})
        
        if not valid_number(data['numero_celular']):
            raise serializers.ValidationError({'numero_celular': 'Should follow this pattern: XX XXXXX-XXXX'})
        
        if not valid_state(data['estado']):
            raise serializers.ValidationError({'estado':'Should be one in the state list'})
        
        if not valid_sex(data['sexo']):
            raise serializers.ValidationError({'sexo':'Should be either M or F'})

        return data
        

