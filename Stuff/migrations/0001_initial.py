# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('partID', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('partCount', models.IntegerField(verbose_name='Ilość')),
                ('partDescription', models.CharField(max_length=800, verbose_name='Opis')),
                ('partType', models.CharField(max_length=100, verbose_name='Typ')),
            ],
        ),
        migrations.CreateModel(
            name='part_document',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='part_picture',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('partID', models.ForeignKey(to='Stuff.Part')),
            ],
        ),
        migrations.CreateModel(
            name='PartDocuments',
            fields=[
                ('docID', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('docFile', models.FileField(upload_to='')),
                ('docLabel', models.CharField(max_length=100, verbose_name='Etykieta')),
            ],
        ),
        migrations.CreateModel(
            name='PartPicture',
            fields=[
                ('pictureID', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('picture', models.ImageField(upload_to='')),
                ('picLabel', models.CharField(max_length=100, verbose_name='Etykieta')),
            ],
        ),
        migrations.AddField(
            model_name='part_picture',
            name='picID',
            field=models.ForeignKey(to='Stuff.PartPicture'),
        ),
        migrations.AddField(
            model_name='part_document',
            name='docID',
            field=models.ForeignKey(to='Stuff.PartDocuments'),
        ),
        migrations.AddField(
            model_name='part_document',
            name='partID',
            field=models.ForeignKey(to='Stuff.Part'),
        ),
    ]
