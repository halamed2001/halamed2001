# Generated by Django 4.0.3 on 2023-04-22 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_donneur_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donneur',
            name='user',
        ),
    ]
