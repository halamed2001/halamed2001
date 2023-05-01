from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm
from .models import Donneur, Hopital, Rendez_vous,Login
from mysite import models

class DonneurForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='كلمة السر')
    class Meta:
        model = Donneur
        fields = '__all__'
        


class HopitalForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput, label='كلمة السر')
   class Meta:
        model = Hopital
        fields = '__all__'
        

class RendezVousForm(forms.ModelForm):
   class Meta:
        model = Rendez_vous
        fields = '__all__'

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='كلمة السر')
    class Meta:
        model = Donneur
        fields = ('nom','password')        


class UpdateProfile(forms.ModelForm):
    nom = forms.CharField(max_length=250, label='الاسم')
    tel = forms.IntegerField( label='الهاتف')
    groupeSanguin = forms.CharField(max_length=250, label='زمرةالدم')
    date_Dernier_Don = forms.CharField(max_length=250, label='تاريخ اخر تبرع')
    

    class Meta:
        model = Donneur
        fields = ('nom', 'tel', 'groupeSanguin', 'date_Dernier_Don')


class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0 direction:RTL'}), label="كلمة المرور القديمة :")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="كلمة المرور الجديدة :")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="تأكيد كلمة المرور :")
    class Meta:
        model = Donneur
        fields = ('old_password','new_password1', 'new_password2')
