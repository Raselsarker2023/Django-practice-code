# Generated by Django 5.0 on 2023-12-27 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musician', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musicianmodel',
            old_name='First_Name',
            new_name='Musician_Name',
        ),
        migrations.RemoveField(
            model_name='musicianmodel',
            name='Last_Name',
        ),
    ]