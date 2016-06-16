# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data_criacao',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data_publicacao',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='texto',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
    ]
