from django.contrib import admin
from mysite.models import Donneur, Hopital, Rendez_vous, Login

# Register your models here.
admin.site.register(Donneur)
admin.site.register(Hopital)
admin.site.register(Rendez_vous)
admin.site.register(Login)