# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requirement', '0003_auto_20151027_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugsOnLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4')),
                ('pd_owner', models.CharField(max_length=20, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba', blank=True)),
                ('bug_status', models.CharField(max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
        migrations.AlterField(
            model_name='requirement',
            name='enroll_date',
            field=models.DateField(auto_now_add=True, verbose_name=b'\xe5\xbd\x95\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
