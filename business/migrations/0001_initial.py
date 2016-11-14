# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-04 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=11)),
                ('details', models.TextField()),
                ('reseller', models.CharField(max_length=11)),
                ('reseller_mob', models.IntegerField(max_length=11)),
                ('storages', models.CharField(max_length=11)),
                ('products', models.CharField(max_length=11)),
                ('start_time', models.DateTimeField()),
                ('dead_time', models.DateTimeField()),
                ('arrived_time', models.CharField(max_length=100, null=True)),
                ('status', models.IntegerField(max_length=11)),
                ('location', models.CharField(max_length=100)),
                ('receive_mode', models.IntegerField(default=2, max_length=11)),
                ('seq', models.IntegerField(default=0, max_length=11)),
                ('card_title', models.CharField(max_length=100)),
                ('card_desc', models.CharField(max_length=255)),
                ('card_icon', models.ImageField(blank=True, upload_to='images/card_icon/%Y/%m/%d')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('volume', models.CharField(max_length=200)),
            ],
        ),
    ]
