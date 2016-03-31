# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stuff', '0003_auto_20160328_0946'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='part_document',
            new_name='part_has_document',
        ),
        migrations.RenameModel(
            old_name='part_picture',
            new_name='part_has_picture',
        ),
        migrations.AlterField(
            model_name='part',
            name='partType',
            field=models.CharField(max_length=100, choices=[('screen', 'Wyświetlacz'), ('sensor', 'Czujnik'), ('uc', 'Mikrokontroler'), ('other', 'Inne'), ('connection', 'Komunikacja'), ('resistors', 'Rezystory'), ('motor', 'Silnik'), ('board', 'Układy scalone'), ('multimedia', 'Media')], verbose_name='Typ'),
        ),
    ]
