from django.shortcuts import render, redirect
from mysite.models import Donneur, Hopital, Login
from mysite import forms, models
from mysite.forms import DonneurForm, HopitalForm


# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')

def donneur(request):
    if request.method == 'POST':
      dataForm = DonneurForm(request.POST)
      dataForm.attrs={'class':'form-control'}
      if dataForm.is_valid():
          dataForm.save()
          msg = 'شكرا! لقد تم تسجيلك' 
    return render(request, 'mysite/donneur.html', {'df':DonneurForm} )

def search(request):
    return render(request, 'mysite/search.html')


def login(request):

    return render(request, 'mysite/login.html')

def register(request):

    return render(request, 'mysite/register.html')


def about(request):
    return render(request, 'mysite/about.html')

def contact(request):
    return render(request, 'mysite/contact.html')

def hopital(request):
    #nom = request.POST.get('nom')
    #password = request.POST.get('password')
    #dt = Hopital(nom=nom, password=password)
    #dt.save()
    return render(request, 'mysite/hopital.html',{'hf':HopitalForm})

def detail(request):
    return render(request, 'mysite/detail.html')


def profil(request):
    return render(request, 'mysite/profil.html')


