# Generated by Django 4.2.5 on 2024-03-04 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_teams_rename_name_leaderboard_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='score',
        ),
    ]
