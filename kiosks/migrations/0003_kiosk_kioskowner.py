# Generated by Django 3.1 on 2020-09-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kiosks', '0002_auto_20200910_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28)),
                ('date_opened', models.DateField()),
                ('street_address', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=8)),
                ('phone_number', models.IntegerField()),
                ('business_type', models.CharField(max_length=28)),
            ],
        ),
        migrations.CreateModel(
            name='KioskOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=6)),
                ('phone_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('id_number', models.IntegerField()),
                ('profile_picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
