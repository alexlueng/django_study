# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 15:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurants_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='restaurants',
            new_name='RestaurantLocation',
        ),
    ]
