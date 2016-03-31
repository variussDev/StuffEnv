# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stuff', '0002_part_partname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='partCount',
            field=models.PositiveIntegerField(verbose_name='Ilość'),
        ),
        migrations.AlterField(
            model_name='part',
            name='partDescription',
            field=models.TextField(max_length=800, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='partpicture',
            name='picture',
            field=models.ImageField(verbose_name='Zdjęcie', upload_to=''),
        ),
    ]
