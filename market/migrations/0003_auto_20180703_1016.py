# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-03 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20180703_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='isfile',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User'),
        ),
    ]
