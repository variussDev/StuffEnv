# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stuff', '0005_auto_20160401_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part_has_picture',
            old_name='partID',
            new_name='part',
        ),
        migrations.RenameField(
            model_name='part_has_picture',
            old_name='picID',
            new_name='pic',
        ),
    ]
