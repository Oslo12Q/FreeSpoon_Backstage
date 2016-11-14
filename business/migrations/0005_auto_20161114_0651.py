# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20161114_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='detailed',
            field=models.IntegerField(default=1992, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_price',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_time',
            field=models.IntegerField(max_length=11),
        ),
    ]
