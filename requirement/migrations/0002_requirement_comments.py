# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('requirement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='comments',
            field=models.TextField(null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
    ]
