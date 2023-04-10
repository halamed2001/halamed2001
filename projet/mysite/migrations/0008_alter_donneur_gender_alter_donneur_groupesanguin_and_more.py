# Generated by Django 4.0.3 on 2023-04-08 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_remove_hopital_pasword_hopital_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donneur',
            name='gender',
            field=models.CharField(choices=[(' 1', 'ذكر'), ('2', 'أنثى')], max_length=10, verbose_name='الجنس'),
        ),
        migrations.AlterField(
            model_name='donneur',
            name='groupeSanguin',
            field=models.CharField(choices=[('1', 'لا اعرف'), ('2', 'o-'), ('3', 'o+'), ('4', 'A-'), ('5', 'B-'), ('6', 'AB-'), ('7', 'B+'), ('8', 'AB+'), ('9', 'A+')], max_length=10, verbose_name='زمرةالدم'),
        ),
        migrations.AlterField(
            model_name='donneur',
            name='wilaya',
            field=models.CharField(choices=[(' 1', 'الحوض الشرقي'), (' 2', 'الحوض الغربي'), ('3', 'لعصابة'), ('4', 'كوركول'), ('5', 'لبراكنة'), ('6', 'ترارزة'), ('7', 'أدرار'), ('8', 'انواذيبو'), ('9', 'تكانت'), ('10', 'غيديماغا'), (' 11', 'تيرس زمور'), ('12', 'إنشيري'), ('13', 'انواكشوط')], max_length=30, verbose_name='الولاية'),
        ),
    ]