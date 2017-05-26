# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170525_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ref',
            field=models.CharField(max_length=200, default='ref'),
            preserve_default=False,
        ),
    ]
