# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-30 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0054_auto_20171130_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='backfill_material',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Backfill Material'),
        ),
        migrations.AddField(
            model_name='well',
            name='sealant_material',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Sealant Material'),
        ),
    ]
