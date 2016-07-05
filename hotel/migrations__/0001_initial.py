# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buchung',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('zimmer_id', models.IntegerField()),
                ('nutzer', models.TextField(verbose_name='Nutzername')),
                ('anzahl_tage', models.IntegerField()),
                ('datum_von', models.DateTimeField()),
                ('datum_bis', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='zimmer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('zimmer', models.TextField(verbose_name='Zimmername')),
                ('preis', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
