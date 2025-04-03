# Create your views here.

from django.shortcuts import render
from .models import Evento

def home(request):
    evento = Evento.objects.first()  # Obtener el primer evento
    return render(request, 'invitacion/home.html', {'evento': evento})
