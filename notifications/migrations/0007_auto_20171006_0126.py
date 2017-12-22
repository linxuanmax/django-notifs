# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_auto_20171005_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='obj',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]