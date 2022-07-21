from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Antropometria, Dexa, Testes
from .forms import AntropometriaForm, TestesForm, DexaForm

def home(request):

    return render(request, 'home.html', {})

def userlist(request):
    antropometrialist = Antropometria.objects.all()
    dexalist = Dexa.objects.all()
    testeslist = Testes.objects.all()

    return render(request, 'userlist.html', {
        'antropometrialist': antropometrialist, 'dexalist': dexalist, 'testeslist': testeslist})

def antropometria(request, n_user):
    antropometriauser = Antropometria.objects.get(n_user=n_user)
    form = AntropometriaForm(request.POST or None, instance=antropometriauser)
    if form.is_valid():
        form.save()
        messages.success(request, ("Dados antropometricos salvos"))
        return redirect('userlist')

    return render(request, 'antropometria.html', {
        'antropometriauser': antropometriauser, 'form': form})


def testes(request, n_user):
    testesuser = Testes.objects.get(n_user=n_user)
    form = TestesForm(request.POST or None, instance=testesuser)
    if form.is_valid():
        form.save()
        messages.success(request, ("Dados dos testes salvos"))
        return redirect('userlist')

    return render(request, 'testes.html', {
        'testesuser': testesuser, 'form': form})

def dexa(request, n_user):
    dexauser = Dexa.objects.get(n_user=n_user)
    form = DexaForm(request.POST or None, instance=dexauser)
    if form.is_valid():
        form.save()
        messages.success(request, ("Dados do DEXA salvos"))
        return redirect('userlist')

    return render(request, 'dexa.html', {
        'dexauser': dexauser, 'form': form})
