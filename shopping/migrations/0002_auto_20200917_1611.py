# Generated by Django 3.1 on 2020-09-17 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20200917_1611'),
        ('customers', '0001_initial'),
        ('shipping', '0001_initial'),
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping.shippingprovider'),
        ),
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.order'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(max_length=50),
        ),
    ]