# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=264, unique=True),
        ),
    ]