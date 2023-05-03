# Generated by Django 4.1 on 2023-04-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0014_playergame_dzfo_successful_playergame_dzfo_taken_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamtourney',
            name='dzfo_cx_per_10_wins',
        ),
        migrations.RemoveField(
            model_name='teamtourney',
            name='dzfo_shots_against_per_10_losses',
        ),
        migrations.RemoveField(
            model_name='teamtourney',
            name='ozfo_cx_against_per_10_losses',
        ),
        migrations.RemoveField(
            model_name='teamtourney',
            name='ozfo_shots_per_10_wins',
        ),
        migrations.AddField(
            model_name='playergame',
            name='fe',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='fx',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='ue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='ux',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playertourney',
            name='fe_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playertourney',
            name='fx_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playertourney',
            name='ue_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playertourney',
            name='ux_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='dzfo_successful',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='dzfo_taken',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='fe',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='fe_against',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='fo_successful',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='fx',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='nzfo_successful',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='nzfo_taken',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='ozfo_successful',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='ozfo_taken',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='successful_passes',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='total_passes',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='ue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='ue_against',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamgame',
            name='ux',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='dzfo_successful_gp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='dzfo_taken_gp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fe_against_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fe_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fo_successful_gp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fx_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='nzfo_successful_gp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='nzfo_taken_gp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ozfo_successful_gp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ozfo_taken_gp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='pass_completion',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='successful_passes_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='total_passes_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ue_against_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ue_gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ux_gp',
            field=models.FloatField(blank=True, null=True),
        ),
    ]