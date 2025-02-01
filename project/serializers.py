from rest_framework import serializers
from .models import Vulnerabilidad

class vulnerabilityserializers(serializers.ModelSerializer):
    class Meta:
        model = Vulnerabilidad
        fields = '__all__' 

class vulnerabilityserializersfilter(serializers.ModelSerializer):
    class Meta:
        model = Vulnerabilidad
        fields = '__all__' 
        
        
class vulnerabilityserializersnofix(serializers.ModelSerializer):
    class Meta:
        model = Vulnerabilidad
        fields = '__all__' 

class vulnerabilityserializersseve(serializers.Serializer):
    Bseverity = serializers.CharField()
    count = serializers.IntegerField()
   
        