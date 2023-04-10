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
    nom = forms.CharField(max_length=250,help_text="The Username field is required.")
    tel = forms.EmailField(max_length=250,help_text="The Email field is required.")
    groupeSanguin = forms.CharField(max_length=250,help_text="The First Name field is required.")
    date_Dernier_Don = forms.CharField(max_length=250,help_text="The Last Name field is required.")
    password = forms.CharField(max_length=250)

    class Meta:
        model = Donneur
        fields = ('nom', 'tel', 'groupeSanguin', 'date_Dernier_Don')

    def clean_password(self):
        if not self.instance.check_password(self.cleaned_data['password']):
            raise forms.ValidationError(f"Password is Incorrect")

    def clean_nom(self):
        nom = self.cleaned_data['nom']
        try:
            donneur = Donneur.objects.exclude(id=self.cleaned_data['id']).get(nom = nom)
        except Exception as e:
            return nom
        raise forms.ValidationError(f"The {donneur.nom} mail is already exists/taken")
    

class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0 direction:RTL'}), label="كلمة المرور القديمة :")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="كلمة المرور الجديدة :")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="تأكيد كلمة المرور :")
    class Meta:
        model = Donneur
        fields = ('old_password','new_password1', 'new_password2')
