from django.urls import path

from . import views

urlpatterns = [
    path('cpu/', views.cpu_list),
    path('allcpu/', views.all_cpu_list)
]