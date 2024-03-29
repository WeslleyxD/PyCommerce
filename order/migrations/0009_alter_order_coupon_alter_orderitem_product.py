# Generated by Django 4.1.2 on 2023-01-31 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0004_coupon_perfil'),
        ('products', '0001_initial'),
        ('order', '0008_remove_order_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='coupon.coupon'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.product'),
        ),
    ]
