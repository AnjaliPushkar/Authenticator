from django.shortcuts import render, redirect, get_object_or_404
from .models import A_data
from django.contrib.auth.models import User, auth
from django.contrib import auth
# Create your views here.
def company(request):
    return render(request, 'employee/company.html')

def A(request):
    return render(request, 'employee/A.html')

def insert(request):
    if request.method == 'POST':
        if request.POST['certi_no'] and request.POST['name'] and request.POST['cname'] and request.POST['fname'] and request.FILES['image']:
                A = A_data()
                A.certi_no = request.POST['certi_no']
                A.name = request.POST['name']
                A.cname = request.POST['cname']
                A.fname = request.POST['fname']
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
