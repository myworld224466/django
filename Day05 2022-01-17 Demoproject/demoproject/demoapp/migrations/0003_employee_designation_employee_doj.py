# Generated by Django 4.0.1 on 2022-01-24 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(choices=[('IT Manager', 'IT Manager'), ('Supervisor', 'Supervisor'), ('Developer', 'Developer')], default='Developer', max_length=50, verbose_name='Designation'),
        ),
        migrations.AddField(
            model_name='employee',
            name='doj',
            field=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Date of Joining'),
        ),
    ]