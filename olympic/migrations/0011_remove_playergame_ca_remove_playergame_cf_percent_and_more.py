# Generated by Django 4.1 on 2023-04-30 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0010_remove_shots_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playergame',
            name='CA',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='CF_percent',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='shots_against',
        ),
        migrations.RemoveField(
            model_name='playertourney',
            name='CA_gp',
        ),
        migrations.RemoveField(
            model_name='playertourney',
            name='CA_gp_percentile',
        ),
        migrations.RemoveField(
            model_name='playertourney',
            name='CF_percent',
        ),
        migrations.RemoveField(
            model_name='playertourney',
            name='CF_percent_percentile',
        ),
        migrations.RemoveField(
            model_name='playertourney',
            name='shots_against_gp',
        ),
    ]
