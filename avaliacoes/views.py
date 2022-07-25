from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Testes_medidas
from .forms import AntropometriaForm, TestesForm, DexaForm, CadastroForm

def home(request):

    return render(request, 'home.html', {})

def users(request, user_id):
    users = Testes_medidas.objects.get(pk=user_id)

    return render(request, 'users.html', {
        'users': users})

def newuser(request):
    submitted = False
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newuser?submitted=True')
    else:
        form = CadastroForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'newuser.html', {'form': form, 'submitted': submitted})


def userlist(request):
    userlist = Testes_medidas.objects.all()

    return render(request, 'userlist.html', {
        'userlist': userlist})

def antropometria(request, user_id):
    antropometriauser = Testes_medidas.objects.get(pk=user_id)
    form = AntropometriaForm(request.POST or None, instance=antropometriauser)
    if form.is_valid():
        form.save()
        messages.success(request, ("Dados antropometricos salvos"))
        return redirect('userlist')

    return render(request, 'antropometria.html', {
        'antropometriauser': antropometriauser, 'form': form})


def testes(request, user_id):
    testesuser = Testes_medidas.objects.get(pk=user_id)
    form = TestesForm(request.POST or None, instance=testesuser)
    if form.is_valid():
        form.save()
        messages.success(request, ("Dados dos testes salvos"))
        return redirect('userlist')

    return render(request, 'testes.html', {
        'testesuser': testesuser, 'form': form})

def dexa(request, user_id):
    dexauser = Testes_medidas.objects.get(pk=user_id)
    form = DexaForm(request.POST or None, instance=dexauser)
    if form.is_valid():
        form.save()
        messages.success(request, ("Dados do DEXA salvos"))
        return redirect('userlist')

    return render(request, 'dexa.html', {
        'dexauser': dexauser, 'form': form})
