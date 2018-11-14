# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-15 09:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0005_auto_20180416_1318'),
        ('oppia', '0013_auto_20180413_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityGamificationPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created')),
                ('points_type', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oppia.Activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity Gamification Points',
                'verbose_name_plural': 'Activity Gamification Points',
            },
        ),
        migrations.CreateModel(
            name='CourseGamificationPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created')),
                ('points_type', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oppia.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Course Gamification Points',
                'verbose_name_plural': 'Course Gamification Points',
            },
        ),
        migrations.CreateModel(
            name='MediaGamificationPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created')),
                ('points_type', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oppia.Media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Media Gamification Points',
                'verbose_name_plural': 'Media Gamification Points',
            },
        ),
        migrations.CreateModel(
            name='QuizGamificationPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created')),
                ('points_type', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quiz Gamification Points',
                'verbose_name_plural': 'Quiz Gamification Points',
            },
        ),
    ]
