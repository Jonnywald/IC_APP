# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20171108_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_Pergunta', models.IntegerField(unique=True)),
                ('Resposta', models.IntegerField()),
            ],
        ),
    ]
