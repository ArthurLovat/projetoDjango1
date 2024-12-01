from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Cuidador

def index(request):
    cuidadores = Cuidador.objects.all()
    context = {
        'curso': 'Programação web com Django framework',
        'outro': 'Django é massa',
        'cuidadores': cuidadores # use essa class para exemplificar a do curso
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
