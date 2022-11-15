from django.db import models

class Cpus(models.Model):
    cpu_name = models.CharField(max_length=20)
    cpu_manufacturer = models.CharField(max_length=20)
    cpu_architecture = models.CharField(max_length=20)
    cpu_cores = models.IntegerField()
    cpu_threads = models.IntegerField()
    cpu_clock = models.FloatField()
    cpu_turbo = models.FloatField()
    cpu_tdp = models.IntegerField()
    def __str__(self):
        return self.cpu_name

