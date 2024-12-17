from rest_framework import serializers
from .models import Inscrito, Institucion

class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'
