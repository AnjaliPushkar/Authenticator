from django.shortcuts import render, redirect, get_object_or_404
from .models import A_data
from django.contrib.auth.models import User, auth
from django.contrib import auth
# Create your views here.
def company(request):
    return render(request, 'employee/company.html')

def A(request):
    employee = A_data.objects
    # return render(request, 'blog/home2.html', {'blog':blog})
    return render(request, 'employee/A.html', {'employee':employee})

def insert(request):
    if request.method == 'POST':
        if request.POST['certi_no'] and request.POST['username'] and request.POST['course'] and request.POST['father'] and request.FILES['image']:
                A = A_data()
                A.certi_no = request.POST['certi_no']
                A.username = request.POST['username']
                A.course = request.POST['course']
                A.father = request.POST['father']
                A.image = request.FILES['image']
                A.save()
                return redirect('/employee/' + str(A.id))
                # return redirect('employee/A.html')

                # return render(request, 'employee/A.html')
        else:
                return render(request, 'employee/insertdata.html')
    else:
        return render(request, 'employee/insertdata.html')
    # return render(request, 'employee/insertdata.html')

def detail(request, A_id):
    A = get_object_or_404(A_data, pk=A_id)
    return render(request, 'employee/detail.html', {'A':A})
