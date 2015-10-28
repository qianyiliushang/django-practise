# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('requirement', '0002_requirement_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='enroll_date',
            field=models.DateField(verbose_name=b'\xe5\xbd\x95\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
