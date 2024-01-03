from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def create_school(request):
    if request.method=='POST':
        sn=request.POST['sn']
        sl=request.POST.get('sl')
        sp=request.POST.get('sp')
        SO=school.objects.get_or_create(sname=sn,slocation=sl,sprincipal=sp)[0]
        SO.save()
        return HttpResponse('school Data is Inserted......')
    return render(request,'create_school.html')
    
