# Generated by Django 4.0.3 on 2023-04-21 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0010_delete_wilaya_remove_groupsanguin_volume_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donneur',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]