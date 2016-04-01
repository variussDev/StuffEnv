# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stuff', '0004_auto_20160331_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partpicture',
            name='pictureID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
