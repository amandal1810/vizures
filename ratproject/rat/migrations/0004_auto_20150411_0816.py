# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rat', '0003_auto_20150411_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='cgpa',
            field=models.DecimalField(max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='marks',
            name='sgpa',
            field=models.DecimalField(max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.DecimalField(max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]
