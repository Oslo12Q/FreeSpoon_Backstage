# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_delete',
            field=models.IntegerField(max_length=11),
        ),
    ]