# Generated by Django 2.2.2 on 2020-09-10 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_product_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]