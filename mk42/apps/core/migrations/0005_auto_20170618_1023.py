# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/migrations/0005_auto_20170618_1023.py

# Generated by Django 1.11.2 on 2017-06-18 10:23

from __future__ import unicode_literals

from django.conf import settings
from django.db import (
    migrations,
    models,
)
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_membership"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membership",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="membership", to=settings.AUTH_USER_MODEL, verbose_name="user"),
        ),
    ]
