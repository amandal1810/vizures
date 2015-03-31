# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('roll', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('cgpa', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
