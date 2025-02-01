from .models import Vulnerabilidad
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count
from .serializers import vulnerabilityserializers, vulnerabilityserializersnofix, vulnerabilityserializersseve,vulnerabilityserializersfilter

class vulnerabilityViewSet(viewsets.ModelViewSet):
    serializer_class = vulnerabilityserializers
    queryset = Vulnerabilidad.objects.all()

class vulnerabilityViewSetfilter(viewsets.ModelViewSet):
    serializer_class = vulnerabilityserializersfilter
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()
    
    def update(self, request, pk=None):
        instance = self.get_queryset(pk)
        if not instance:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
            
class vulnerabilityViewSetNoFix(viewsets.ModelViewSet):
    serializer_class = vulnerabilityserializersnofix
    queryset = Vulnerabilidad.objects.exclude(status = 'FIXED') 


class vulnerabilityViewSetseveridad(viewsets.ModelViewSet):
    serializer_class = vulnerabilityserializersseve
    queryset = Vulnerabilidad.objects.values('Bseverity').annotate(count=Count('Bseverity')).order_by('Bseverity')
   

    
        
    

    