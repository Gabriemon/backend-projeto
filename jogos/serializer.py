from rest_framework import serializers
from jogos.models import Jogos




class JogosSerializer(serializers.ModelSerializer):


    class Meta:
        model = Jogos
        fields = ['id','nome', 'data_lancamento', 'preco']