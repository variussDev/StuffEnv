# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stuff', '0006_auto_20160401_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='pictures',
            field=models.ManyToManyField(to='Stuff.PartPicture'),
        ),
    ]
