from django.contrib import auth
from employee.models import A_data
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def check(request):
    return render(request, 'check.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def verify(request):
    return render(request, 'verificationpage.html')

def loginemployee(request):
    return render(request, 'loginemployee.html')

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('certificateno')
        posts = A_data.objects.all().filter(certi_no = search)
        return render(request, 'searchbar.html', {'posts' : posts})
