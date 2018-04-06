# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


def fix_future_dates(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Tracker = apps.get_model('oppia', 'Tracker')
    for tracker in Tracker.objects.filter(tracker_date__gt=timezone.now()):
        tracker.tracker_date = tracker.submitted_date
        tracker.save()

class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0011_auto_20170620_1722'),
    ]

    operations = [
        migrations.RunPython(fix_future_dates),
    ]
