# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stuff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='partName',
            field=models.CharField(max_length=200, blank=True, verbose_name='Nazwa'),
        ),
    ]
