# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-26 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0003_auto_20190720_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('total_consumption', models.DecimalField(decimal_places=2, max_digits=16)),
            ],
        ),
    ]
