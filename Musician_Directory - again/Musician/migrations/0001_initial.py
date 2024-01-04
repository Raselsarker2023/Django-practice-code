# Generated by Django 5.0 on 2023-12-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_no', models.CharField(max_length=15)),
                ('Instrument_Type', models.CharField(max_length=100)),
            ],
        ),
    ]