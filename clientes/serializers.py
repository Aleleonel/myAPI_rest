from clientes.validators import celular_valido, cpf_valido, nome_valido, rg_valido
import clientes
from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields =  '__all__'

    def validate(self, data):

        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF inválido, deve conter 11 digitos"})        
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Nome de ser uma letras"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError("Quantidade de dígitos inválido par o campo RG")
        
        if not celular_valido(data['celular']):
             raise serializers.ValidationError({'celular':"Celular inválido, favor verificar o número e padrão correto xx xxxx-xxxx"})
        
        return data
