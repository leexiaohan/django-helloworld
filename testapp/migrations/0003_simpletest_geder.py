# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20151227_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpletest',
            name='geder',
            field=models.CharField(default='male', max_length=20),
            preserve_default=False,
        ),
    ]
