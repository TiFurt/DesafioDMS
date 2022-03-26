from django.shortcuts import render, redirect
from .models import Time, Disputa
from .forms import TimeForm, DisputaForm


def index(request):
    return render(request, 'index.html')


def create_time(request):
    form = TimeForm(request.POST or None)
    times = Time.objects.all()
    if form.is_valid():
        form.save()


    return render(request, 'new.html', {'form': form, 'times': times})


def delete_times(request):
    times = Time.objects.all()
    times.delete()
    return redirect('create_time')


def disputa(request):
    form = DisputaForm(request.POST or None)
    disputas = Disputa.objects.all()
    if form.is_valid():
        form.save()

    return render(request, 'disputa.html', {'form': form, 'disputas': disputas})


def delete_disputas(request):
    disputas = Disputa.objects.all()

    disputas.delete()
    return redirect('disputa')


def ranking(request):
    disputas = Disputa.objects.all()
    resultado = {}
    for disputa in disputas:
        time01 = disputa.time01
        time02 = disputa.time02
        if time01.nome in resultado:
            resultado[time01.nome] += disputa.gols01
        else:
            resultado[time01.nome] = disputa.gols01
        if time02.nome in resultado:
            resultado[time02.nome] += disputa.gols02
        else:
            resultado[time02.nome] = disputa.gols02
    sortedDict = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
    return render(request, 'ranking.html', {'resultado': sortedDict})
