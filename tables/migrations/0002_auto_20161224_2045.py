# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='duties',
            field=models.CharField(db_column='duties', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_name',
            field=models.CharField(db_column='post_name', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='requirements',
            field=models.CharField(db_column='requirements', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='salary',
            field=models.CharField(db_column='salary', max_length=20),
        ),
        migrations.AlterField(
            model_name='worker',
            name='address',
            field=models.CharField(db_column='address', max_length=200),
        ),
        migrations.AlterField(
            model_name='worker',
            name='age',
            field=models.IntegerField(db_column='age'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='full_name',
            field=models.CharField(db_column='fullname', max_length=100),
        ),
        migrations.AlterField(
            model_name='worker',
            name='gender',
            field=models.CharField(db_column='gender', max_length=15),
        ),
        migrations.AlterField(
            model_name='worker',
            name='passport',
            field=models.CharField(db_column='passport', max_length=10),
        ),
        migrations.AlterField(
            model_name='worker',
            name='phone',
            field=models.CharField(db_column='w_phone', max_length=20),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_id',
            field=models.AutoField(db_column='w_id', primary_key=True, serialize=False),
        ),
    ]
