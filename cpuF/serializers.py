from .models import Cpus
from rest_framework import serializers


class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpus
        fields = ('cpu_name', 'cpu_manufacturer', 'cpu_architecture', 'cpu_cores', 'cpu_threads', 'cpu_clock', 'cpu_turbo', 'cpu_tdp')
