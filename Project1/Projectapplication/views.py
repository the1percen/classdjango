from django.shortcuts import render,redirect
from pathlib import Path
import os
# Create your views here.
from .models import registration
from django.http import HttpResponse
from django.contrib import sessions

BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    #return HttpResponse("Welcome to django")
    result = os.path.join(BASE_DIR,"templates")
    print(result)
    vari = registration.objects.get(id=1)
    new_vari = vari.email
    request.session['email'] = new_vari
    return render(request,"index.html",{'name':new_vari})

def summa(request):
    var1 = request.POST["Email Address"]
    var2 = request.POST["Phone Number"]
    myobj=registration()
    myobj.email=var1
    myobj.phone_number=var2
    myobj.save()
    vari = registration.objects.get()
    return render(request,"home.html",{'name':var1})
#python manage.py runserver
#python manage.py makemigrations Projectapplication

def summa1(request):
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1 
    vari = registration.objects.all()
    new_vari = request.session['email']
    return render(request, 'summa.html', {'name': new_vari})

def summa2(request):
    request.session['email'] = ''
    return render(request, 'summa2.html', {'name':request.session['email']})