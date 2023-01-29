# Generated by Django 4.1.2 on 2023-01-29 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_alter_coupon_perfil'),
        ('order', '0002_order_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coupon', to='coupon.coupon'),
        ),
    ]
