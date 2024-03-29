# Generated by Django 4.0.3 on 2023-04-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_remove_donneur_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donneur',
            name='groupeSanguin',
            field=models.CharField(choices=[('لا اعرف', 'لا اعرف'), ('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('B+', 'B+'), ('AB+', 'AB+'), ('A+', 'A+')], max_length=10, verbose_name='زمرةالدم'),
        ),
        migrations.AlterField(
            model_name='donneur',
            name='wilaya',
            field=models.CharField(choices=[(' الحوض الشرقي', 'الحوض الشرقي'), ('الحوض الغربي', 'الحوض الغربي'), ('لعصابة', 'لعصابة'), ('كوركول', 'كوركول'), ('لبراكنة', 'لبراكنة'), ('ترارزة', 'ترارزة'), ('أدرار', 'أدرار'), ('انواذيبو', 'انواذيبو'), ('تكانت', 'تكانت'), ('كيديماغا', 'كيديماغا'), ('تيرس زمور', 'تيرس زمور'), ('إنشيري', 'إنشيري'), ('انواكشوط', 'انواكشوط')], max_length=30, verbose_name='الولاية'),
        ),
    ]
