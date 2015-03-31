# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub1', models.IntegerField(default=0)),
                ('sub2', models.IntegerField(default=0)),
                ('sub3', models.IntegerField(default=0)),
                ('sub4', models.IntegerField(default=0)),
                ('sub5', models.IntegerField(default=0)),
                ('lab1', models.IntegerField(default=0)),
                ('lab2', models.IntegerField(default=0)),
                ('lab3', models.IntegerField(default=0)),
                ('sgpa', models.DecimalField(max_digits=4, decimal_places=2)),
                ('cgpa', models.DecimalField(max_digits=4, decimal_places=2)),
                ('sem_credits', models.IntegerField(default=0)),
                ('total_credits', models.IntegerField(default=0)),
                ('remarks', models.CharField(max_length=10)),
                ('reg_no', models.ForeignKey(to='rat.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('sem', models.IntegerField(serialize=False, primary_key=True)),
                ('sub1', models.CharField(max_length=50)),
                ('sub2', models.CharField(max_length=50)),
                ('sub3', models.CharField(max_length=50)),
                ('sub4', models.CharField(max_length=50)),
                ('sub5', models.CharField(max_length=50)),
                ('lab1', models.CharField(max_length=50)),
                ('lab2', models.CharField(max_length=50)),
                ('lab3', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='marks',
            name='sem',
            field=models.ForeignKey(to='rat.Semester'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default=b'CSE', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='reg_no',
            field=models.IntegerField(default=b'20120000', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.DecimalField(max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
