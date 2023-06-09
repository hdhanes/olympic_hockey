# Generated by Django 4.1 on 2023-04-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0015_remove_teamtourney_dzfo_cx_per_10_wins_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playertourney',
            name='shots_for_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='CA_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='CF_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='CF_percent_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='FA_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='FF_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='FF_percent_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='PDO_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ce_against_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ce_against_rate_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ce_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ce_rate_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='cx_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='cx_rate_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='dzfo_successful_gp_percentile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='dzfo_taken_gp_percentile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='dzfo_win_percent_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fe_against_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fe_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fe_rate_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fo_successful_gp_percentile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fo_taken_gp_percentile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fo_win_percent_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fx_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='fx_rate_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ga_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='gf_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='nzfo_successful_gp_percentile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='nzfo_taken_gp_percentile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='nzfo_win_percent_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ozfo_successful_gp_percentile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ozfo_taken_gp_percentile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ozfo_win_percent_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='pass_completion_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='save_percentage_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='shooting_percent_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='shots_against_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='shots_for_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='shots_share_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='successful_passes_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='total_passes_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ue_against_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ue_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ue_rate_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ux_gp_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='ux_rate_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamtourney',
            name='zone_denial_rate_percentile',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
