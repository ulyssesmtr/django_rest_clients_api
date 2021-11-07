from validate_docbr import CPF
from datetime import datetime
import re

states = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Espirito', 'Goiás', 'Maranhão',
    'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí',
    'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina',
    'São Paulo', 'Sergipe', 'Tocantins', 'Distrito Federal']

def valid_name(name):
    return name.isalpha()

def valid_rg (rg_number):
    return len(rg_number) == 9 and rg_number.isnumeric()

def valid_cpf(cpf_number):
    cpf = CPF()
    return cpf.validate(cpf_number)

def valid_date(date):
    return date < datetime.today().date()

def valid_number(numero):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    return re.findall(model, numero)

def valid_state(estado):
    return estado in states

def valid_sex(sex):
    return sex in ['F', 'M']
