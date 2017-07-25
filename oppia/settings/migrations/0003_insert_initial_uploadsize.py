# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations

from oppia.settings import constants
from oppia.settings.models import SettingProperties


def insert_maxuploadsize(apps, schema_editor):
    current = SettingProperties.get_int(constants.MAX_UPLOAD_SIZE, None)
    if current is None and hasattr(settings, 'OPPIA_MAX_UPLOAD_SIZE'):
        settingProp = SettingProperties()
        settingProp.key = constants.MAX_UPLOAD_SIZE
        settingProp.int_value = settings.OPPIA_MAX_UPLOAD_SIZE
        settingProp.save()

class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20170628_1923'),
    ]

    operations = [
        migrations.RunPython(insert_maxuploadsize),
    ]
