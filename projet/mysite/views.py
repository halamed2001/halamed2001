from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, login as auth_loguin
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages
from django.http import HttpResponse


from mysite.models import Donneur, Hopital, Login
from mysite import forms, models
from mysite.forms import DonneurForm, HopitalForm, RendezVousForm, LoginForm


context={
    'page':'',
    'page_title':'',
    'system_name':'Blood Bank Managament System',
    'has_navigation':True,
    'has_sidebar':True,
}


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
    return render(request, 'mysite/search.html')


def login(request):
    form = LoginForm()
    if request.POST:
        nom = request.POST['nom']
        password = request.POST['password']

        donneur = Donneur(nom=nom, password=password)
        if donneur.is_exist():
            return redirect('profile')

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

@login_required (redirect_field_name='profile')
def profile(request):
    profile = models.Donneur.objects.all()
    return render(request, 'mysite/profil.html')



def update_profile(request):
    context['page_title'] = 'تعديل الصفحة'
    donneur = Donneur.objects.get(id = request.donneur.id)
    if not request.method == 'POST':
        form = forms.UpdateProfile(instance=donneur)
        context['form'] = form
        print(form)
    else:
        form = forms.UpdateProfile(request.POST, instance=donneur)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تعديل الملف الشخصي")
            return redirect("profile")
        else:
            context['form'] = form
            
    return render(request, 'mysite/update_profile.html',context)




def update_password(request):
    context['page_title'] = "تغيير كلمة السر"
    if request.method == 'POST':
        form = forms.UpdatePasswords(donneur = request.donneur, data= request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Account Password has been updated successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
        else:
            context['form'] = form
    else:
        form = forms.UpdatePasswords(request.POST)
        context['form'] = form
    return render(request,'mysite/update_password.html',context)