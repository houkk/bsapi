# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.utils import timezone
from django.db import models, migrations


def create_unique_timestamp(apps, schema_editor):
    UserBook = apps.get_model('ownership', 'UserBook')

    for userbook in UserBook.objects.all():
        delta = timezone.timedelta(days=random.randint(1,1000))
        userbook.created_at = timezone.now() - delta
        userbook.save()

def ignore_timestamp(*args, **kwargs):
    pass



class Migration(migrations.Migration):

    dependencies = [
        ('ownership', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_unique_timestamp, ignore_timestamp),
    ]
