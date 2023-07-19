from django.shortcuts import render, redirect
from .models import Carro

def criar_carro(request):
    if request.method == 'POST':
        modelo1 = request.POST.get('modelo')
        marca2 = request.POST.get('marca')
        placa3 = request.POST.get('placa')
        tipo4 = request.POST.get('tipo')

        carro = Carro(
        modelo=modelo1, 
        marca=marca2,
        placa=placa3,
        tipo=tipo4,
        )
        carro.save()

        return redirect('carros_form')
    
    else:
        return render(request, 'main/index.html')