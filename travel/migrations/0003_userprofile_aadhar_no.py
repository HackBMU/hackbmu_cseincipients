# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-06 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20180406_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='aadhar_no',
            field=models.CharField(default=123456789123, max_length=12),
            preserve_default=False,
        ),
    ]
