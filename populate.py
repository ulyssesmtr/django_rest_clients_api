import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random, datetime
from clients_api.models import Cliente

def creating_clients(quantity):
    fake = Faker('pt_BR')
    Faker.seed(10)
    states = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Espirito', 'Goiás', 'Maranhão',
    'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí',
    'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina',
    'São Paulo', 'Sergipe', 'Tocantins', 'Distrito Federal']

    for n in range(quantity):
        nome = fake.name()
        rg = f'{random.randrange(100,999)}{random.randrange(100,999)}{random.randrange(100,999)}'
        cpf = CPF()
        cpf = cpf.generate()
        data_nascimento = fake.date_between(start_date='-18y', end_date='today')
        numero_celular = f'{random.randrange(10,55)} 9{random.randrange(1000,9999)}-{random.randrange(1000,9999)}'
        estado = random.choice(states)
        sexo = random.choice(['M', 'F'])
        c = Cliente.objects.create(nome=nome, rg=rg, cpf=cpf, data_nascimento=data_nascimento, numero_celular=numero_celular, estado=estado, sexo=sexo)
        c.save()

creating_clients(500)