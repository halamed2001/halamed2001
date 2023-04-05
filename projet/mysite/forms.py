from django import forms
from .models import Donneur

class DonneurForm(forms.ModelForm):
     class Meta:
        model = Donneur
        fields = '__all__'
        


class HopitalForm(forms.Form):
    الاسم = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    كلمة_السر = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

class RendezVousForm(forms.Form):
    اليوم = forms.CharField(required=True, widget=forms.TextInput())
    المكان = forms.CharField(required=True, widget=forms.TextInput())


