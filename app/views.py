from django.shortcuts import render
from app.models import *
# Create your views here.
 
def department(request):
    QLDO=Dept.objects.all()
    d={'depts' : QLDO}
    return render(request,'department.html',d)

def employee(request):
    QLEO=Emp.objects.all()
    d={'emp' : QLEO}
    return render(request,'employee.html',d)