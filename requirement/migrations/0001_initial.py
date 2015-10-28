# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enroll_date', models.DateTimeField(default=django.utils.timezone.now,
                                                     verbose_name=b'\xe5\xbd\x95\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4')),
                ('pd_owner', models.CharField(max_length=20,
                                              verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('business_type',
                 models.CharField(max_length=100, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe7\xb1\xbb\xe5\x9e\x8b')),
                (
                'requirement_desc', models.TextField(verbose_name=b'\xe9\x9c\x80\xe6\xb1\x82\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('solution', models.TextField(verbose_name=b'\xe8\xa7\xa3\xe5\x86\xb3\xe6\x96\xb9\xe6\xa1\x88')),
                ('estimate_solute_date', models.DateField(
                    verbose_name=b'\xe9\xa2\x84\xe8\xae\xa1\xe8\xa7\xa3\xe5\x86\xb3\xe6\x97\xb6\xe9\x97\xb4')),
                ('actual_solute_date', models.DateField(null=True,
                                                        verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe8\xa7\xa3\xe5\x86\xb3\xe6\x97\xb6\xe9\x97\xb4',
                                                        blank=True)),
                ('requirement_type',
                 models.CharField(max_length=100, verbose_name=b'\xe9\x9c\x80\xe6\xb1\x82\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('requirement_source',
                 models.CharField(max_length=100, verbose_name=b'\xe9\x9c\x80\xe6\xb1\x82\xe6\x9d\xa5\xe6\xba\x90')),
                ('requirement_status',
                 models.CharField(max_length=100, verbose_name=b'\xe9\x9c\x80\xe6\xb1\x82\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
    ]
