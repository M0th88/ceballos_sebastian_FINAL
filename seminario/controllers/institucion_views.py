from django.shortcuts import render, get_object_or_404
from ..models import Institucion
from django.http import JsonResponse

def institucion_list(request):
    instituciones = Institucion.objects.all()
    return render(request, 'institucion_list.html', {'instituciones': instituciones})

def institucion_detail(request, id):
    institucion = get_object_or_404(Institucion, pk=id)
    return JsonResponse({'id': institucion.id, 'nombre': institucion.nombre})
