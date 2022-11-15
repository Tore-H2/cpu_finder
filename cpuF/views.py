from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cpus
from .serializers import CpuSerializer
from django.http import JsonResponse


@api_view(['POST'])
def cpu_list(request):
    snippets = Cpus.objects.all()
    cpu = snippets.filter(cpu_name=request.data['cpu_name'])
    serializer = CpuSerializer(cpu, many=True)
    return JsonResponse({'cpu': serializer.data})
        
@api_view(['GET'])
def all_cpu_list(request):  
    snippets = Cpus.objects.all()
    cpu = list(snippets.values_list("cpu_name"))
    return JsonResponse({"cpu": cpu})
