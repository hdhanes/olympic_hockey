# Generated by Django 4.1 on 2023-04-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0012_playergame_successful_passes_playergame_total_passes'),
    ]

    operations = [
        migrations.AddField(
            model_name='playertourney',
            name='successful_passes_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playertourney',
            name='total_passes_gp',
            field=models.FloatField(blank=True, null=True),
        ),
    ]