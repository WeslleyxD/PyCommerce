# Generated by Django 4.1.2 on 2023-01-29 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_remove_perfil_address_remove_perfil_coupon_and_more'),
        ('coupon', '0003_remove_coupon_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.perfil', verbose_name='Perfil'),
        ),
    ]