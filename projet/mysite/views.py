from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash as auth_loguin
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages,auth
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from mysite.models import Donneur, Hopital, Login
from mysite import forms, models
from mysite.forms import DonneurForm, HopitalForm, RendezVousForm, LoginForm, UpdatePasswords, UpdateProfile





# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')

def donneur(request):
    msg =''
    form = DonneurForm()
    if request.method == 'POST':
        form = DonneurForm(request.POST)
        if form.is_valid():
            donneur = form.save()
            msg = 'شكرا! لقد تم تسجيلك'
    return render(request, 'mysite/donneur.html', {'form':form, 'msg':msg})

def rendez_vous(request):
    form = RendezVousForm()
    msg =''
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rendez_vous = form.save()
            msg = 'شكرا!  تم حجز موعدك نرجوا أن تكون في الموعد'
    return render(request, 'mysite/rendez_vous.html', {'form':form, 'msg':msg})

def search(request):
    donneur = Donneur.objects.all()
    groupeSanguin = None
    if 'search_name' in request.GET:
        groupeSanguin = request.GET['search_name']
        if groupeSanguin:
            donneur = donneur.filter(groupeSanguin__icontains = groupeSanguin)

    context={
    'donneur' : donneur
    }
    return render(request, 'mysite/search.html', context)


def login(request, nom, password):
    form = LoginForm()
    nom = ''
    password = ''
    if request.POST:
        nom = request.POST['nom']
        password = request.POST['password']
        form = LoginForm(request.POST, nom=nom, password=password)
        donneur = authenticate(request, nom=nom, password=password)
        if donneur is not None:
            if donneur.is_active:
                login(request, donneur)
                return redirect('profile') 
            else:
                error_msg = 'خطأ في إسم المستخدم أو كلمة المرور'
        else:
            error_msg = 'خطأ في إسم المستخدم أو كلمة المرور'
            
            return render(request, 'mysite/login.html', {'error_msg':error_msg,'form':form})
    else:
        return render(request, 'mysite/login.html',{'form':form})

def register(request):

    return render(request, 'mysite/register.html')


def about(request):
    return render(request, 'mysite/about.html')

def contact(request):
    return render(request, 'mysite/contact.html')

def hopital(request):
    msg=''
    form = HopitalForm()
    if request.method == 'POST':
        form = HopitalForm(request.POST)
        if form.is_valid():
            hopital = form.save()
            msg = 'شكرا! لقد تم تسجيلك'

    return render(request, 'mysite/hopital.html', {'form':form, 'msg':msg})

def detail(request):
    return render(request, 'mysite/detail.html')

#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request, ):
    donneur = Donneur.objects.all()
    context = {
        'donneur':donneur
    }
    return render(request, 'mysite/profil.html', context)


@login_required
def update_profile(request):
    form = UpdateProfile()
    donneur = Donneur.objects.get(id = request.post.id)  
    if not request.method == 'POST':
        form = UpdateProfile(instance=donneur)    
    return render(request, 'mysite/update_profile.html',{'form':form})



@login_required
def update_password(request):
   form = UpdatePasswords(Donneur)

   return render(request,'mysite/update_password.html',{'form': form})