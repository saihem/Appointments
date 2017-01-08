# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('description', models.TextField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifed_on', models.DateTimeField(null=True)),
            ],
        ),
    ]
