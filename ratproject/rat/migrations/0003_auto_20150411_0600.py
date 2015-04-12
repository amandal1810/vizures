# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rat', '0002_auto_20150331_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='cgpa',
            field=models.DecimalField(max_digits=12, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='marks',
            name='sgpa',
            field=models.DecimalField(max_digits=12, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.DecimalField(max_digits=12, decimal_places=10),
            preserve_default=True,
        ),
    ]
