# Generated by Django 4.1.2 on 2023-01-31 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0006_alter_address_perfil'),
        ('coupon', '0004_coupon_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coupon', to='perfil.perfil'),
        ),
    ]
