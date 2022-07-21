from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Login invalido, tente de novo"))
            return redirect('login')

    else:
         return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Para acessar, logue novamente"))
    return redirect('home')



