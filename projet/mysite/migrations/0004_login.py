# Generated by Django 4.0.3 on 2023-03-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_donneur_options_alter_hopital_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name=' اسم المستخدم')),
                ('password', models.CharField(max_length=20, verbose_name=' كلمة السر')),
            ],
        ),
    ]
