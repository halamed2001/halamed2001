# Generated by Django 4.0.3 on 2023-03-31 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_login'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='login',
            options={'verbose_name': 'اتصال', 'verbose_name_plural': 'اتصالات'},
        ),
        migrations.RemoveField(
            model_name='donneur',
            name='nom',
        ),
    ]
