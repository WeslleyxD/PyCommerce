# Generated by Django 4.1.2 on 2023-01-30 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_address_selected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
    ]
