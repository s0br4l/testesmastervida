from django.shortcuts import render

def home(request):

    return render(request, 'home.html', {})

def medidas(request):

    return render(request, 'medidas.html', {})