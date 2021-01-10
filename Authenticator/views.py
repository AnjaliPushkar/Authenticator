from django.contrib import auth
from employee.models import A_data
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import auth

def home(request):
    return render(request, 'home.html')

def check(request):
    return render(request, 'check.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'verificationpage.html')
        else:
            return render(request, 'login.html', {'error':'user not found..!!'})
    else:
        return render(request, 'login.html')

def loginemployee(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'], key='AO64')
        if user is not None:
            auth.login(request, user)
            return redirect('/employee/A')
            # return render(request, 'employee/A.html')
        else:
            return render(request, 'loginemployee.html', {'error':'user not found..!!'})
    else:
        return render(request, 'loginemployee.html')
    # return render(request, 'login.html')

# def signup(request):
#     return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(email=request.POST['email'])
                return render(request, 'signup.html', {'error': 'Email Id has already been taken'})
            except User.DoesNotExist :
                user = User.objects.create_user(username =request.POST['username'], password =request.POST['password'], email=request.POST['email'])
                auth.login(request, user)
                return render(request, 'login.html')
        else:
            return render(request, 'signup.html', {'error': 'password not matching'})
    else:
        return render(request, 'signup.html')


def verify(request):
    # return redirect('verificy/');
    return render(request, 'verificationpage.html')

# def loginemployee(request):
#     return render(request, 'loginemployee.html')

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('certificateno')
        posts = A_data.objects.all().filter(certi_no = search)
        return render(request, 'searchbar.html', {'posts' : posts})
