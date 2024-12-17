from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from ..models import Inscrito, Institucion
from ..serializers import InscritoSerializer, InstitucionSerializer

# Información del Autor
@api_view(['GET'])
def autor_info(request):
    return Response({
        "autor": "Sebastián",
        "email": "seba_ftw@hotmail.com",
        "Carreara": "Analista Programador",
    })

# API para Inscritos
class InscritoAPI(ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

# API para Instituciones
class InstitucionAPI(ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
