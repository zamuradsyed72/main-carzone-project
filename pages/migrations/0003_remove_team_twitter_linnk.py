# Generated by Django 5.2 on 2025-04-22 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='twitter_linnk',
        ),
    ]
