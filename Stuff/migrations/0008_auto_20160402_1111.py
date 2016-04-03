# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stuff', '0007_part_pictures'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PartDocuments',
            new_name='PartDocument',
        ),
        migrations.RemoveField(
            model_name='part_has_document',
            name='docID',
        ),
        migrations.RemoveField(
            model_name='part_has_document',
            name='partID',
        ),
        migrations.RemoveField(
            model_name='part_has_picture',
            name='part',
        ),
        migrations.RemoveField(
            model_name='part_has_picture',
            name='pic',
        ),
        migrations.DeleteModel(
            name='part_has_document',
        ),
        migrations.DeleteModel(
            name='part_has_picture',
        ),
    ]
