from django.shortcuts import render, redirect, get_object_or_404
from .models import A_data

# Create your views here.
def company(request):
    return render(request, 'employee/company.html')

def A(request):
    # if request.POST['cid'] and request.POST['name'] and request.POST['cname'] and request.POST['fname'] and request.POST['image']:
    #     A = A_data()
    #     A.cid = request.POST['cid']
    #     A.name = request.POST['name']
    #     A.cname = request.POST['cname']
    #     A.fname = request.POST['fname']
    #     A.image = request.POST['image']
    #     A.save()
            return render(request, 'employee/A.html')

def insert(request):
    return render(request, 'employee/insertdata.html')
