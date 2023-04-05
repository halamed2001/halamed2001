from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donneur', views.donneur, name='donneur'),
    path('search', views.search, name='search'),
    path('hopital', views.hopital, name='hopital'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('detail', views.detail, name='detail'),
    path('profil', views.profil, name='profil'),
   

]