# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-14 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_t_apk_system_config'),
    ]

    operations = [
        migrations.CreateModel(
            name='TApkSystemConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(blank=True, max_length=30, null=True)),
                ('version', models.CharField(blank=True, max_length=20, null=True)),
                ('systemsize', models.IntegerField(blank=True, db_column='systemSize', null=True)),
                ('fixedsize', models.IntegerField(blank=True, db_column='fixedSize', null=True)),
                ('surplussize', models.IntegerField(blank=True, db_column='surplusSize', null=True)),
                ('hdversion', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 't_apk_system_config',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='t_apk_system_config',
        ),
    ]
