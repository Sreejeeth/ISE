# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-19 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirmvit', '0002_auto_20180319_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdbs',
            name='USN',
            field=models.TextField(blank=True, max_length=11),
        ),
    ]
