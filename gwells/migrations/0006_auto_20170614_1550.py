# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0005_auto_20170612_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrillingMethod',
            fields=[
                ('drilling_method_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_drilling_method',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='GroundElevationMethod',
            fields=[
                ('ground_elevation_method_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_ground_elevation_method',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='ground_elevation',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='orientation_vertical',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='other_drilling_method',
            field=models.CharField(blank=True, max_length=50, verbose_name='Specify Other Drilling Method'),
        ),
        migrations.AddField(
            model_name='well',
            name='ground_elevation',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='well',
            name='orientation_vertical',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='well',
            name='other_drilling_method',
            field=models.CharField(blank=True, max_length=50, verbose_name='Specify Other Drilling Method'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='drilling_method',
            field=models.ForeignKey(blank=True, db_column='drilling_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.DrillingMethod', verbose_name='Drilling Method'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='ground_elevation_method',
            field=models.ForeignKey(blank=True, db_column='ground_elevation_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.GroundElevationMethod', verbose_name='Method for Determining Ground Elevation'),
        ),
        migrations.AddField(
            model_name='well',
            name='drilling_method',
            field=models.ForeignKey(blank=True, db_column='drilling_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.DrillingMethod', verbose_name='Drilling Method'),
        ),
        migrations.AddField(
            model_name='well',
            name='ground_elevation_method',
            field=models.ForeignKey(blank=True, db_column='ground_elevation_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.GroundElevationMethod', verbose_name='Method for Determining Ground Elevation'),
        ),
    ]