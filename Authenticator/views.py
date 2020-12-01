from django.contrib import auth
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def verify(request):
    return render(request, 'verificationpage.html')

def loginemployee(request):
    return render(request, 'loginemployee.html')
