# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 02:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20171008_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessrecord',
            name='name',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]
