from django.db import models

#a model that will store team metadata
class Teams(models.Model):
    team_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length = 50, blank=True, null=True)
    flag_url = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
#a model that will store player metadata
class Players(models.Model):
    player_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length = 100, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    team_id = models.ForeignKey('Teams', on_delete=models.CASCADE, blank=True, null=True, related_name='players')
    
    def __str__(self):
        return self.name
    
#a model that will store game metadata
class Games(models.Model):
    game_id = models.IntegerField(unique=True, primary_key=True)
    home_team = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='home_team')
    away_team = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='away_team')
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return str(self.game_id)
    
    
 
############################################################################################# 


    
#a base storage model that will record all of the shot attempt data in the dataset
class Shots(models.Model):
    shot_id = models.IntegerField(unique=True, primary_key=True)
    game_id = models.ForeignKey("Games", on_delete=models.CASCADE, related_name='shots')
    period = models.IntegerField(blank=True, null=True)
    periodtime = models.IntegerField(blank=True, null=True)
    gametime = models.IntegerField(blank=True, null=True)
    home_team_skaters = models.IntegerField(blank=True, null=True)
    away_team_skaters = models.IntegerField(blank=True, null=True)
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='shots')
    player_id = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='shots')
    result = models.CharField(max_length=10, blank=True, null=True)
    x_coord = models.IntegerField(blank=True, null=True)
    y_coord = models.IntegerField(blank=True, null=True)
    shot_type = models.CharField(max_length=30, blank=True, null=True)
    traffic = models.CharField(max_length=31, blank=True, null=True)
    one_timer = models.CharField(max_length=30, blank=True, null=True)
    a1 = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='a1')
    a2 = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='a2')
    a3 = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='a3')
    
#a base storage model that will record all of the passing data in the dataset
class Passes(models.Model):
    pass_id = models.IntegerField(unique=True, primary_key=True)
    game_id = models.ForeignKey("Games", on_delete=models.CASCADE, related_name='passes')
    period = models.IntegerField(blank=True, null=True)
    periodtime = models.IntegerField(blank=True, null=True)
    gametime = models.IntegerField(blank=True, null=True)
    home_team_skaters = models.IntegerField(blank=True, null=True)
    away_team_skaters = models.IntegerField(blank=True, null=True)
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='passes')
    success = models.BooleanField(blank=True, null=True)
    pass_type = models.CharField(max_length=31, blank=True, null=True)
    passer_id = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='passes')
    passer_x_coord = models.IntegerField(blank=True, null=True)
    passer_y_coord = models.IntegerField(blank=True, null=True)
    passer_zone = models.CharField(max_length=2, blank=True, null=True)
    receiver_id = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='passes_received')
    receiver_x_coord = models.IntegerField(blank=True, null=True)
    receiver_y_coord = models.IntegerField(blank=True, null=True)
    receiver_zone = models.CharField(max_length=2, blank=True, null=True)
    
#a base storage model that will record all of the takeaway data in the dataset
class Takeaways(models.Model):
    takeaway_id = models.IntegerField(unique=True, primary_key=True)
    game_id = models.ForeignKey("Games", on_delete=models.CASCADE, related_name='takeaways')
    period = models.IntegerField(blank=True, null=True)
    periodtime = models.IntegerField(blank=True, null=True)
    gametime = models.IntegerField(blank=True, null=True)
    home_team_skaters = models.IntegerField(blank=True, null=True)
    away_team_skaters = models.IntegerField(blank=True, null=True)
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='takeaways')
    player_id = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='takeaways')
    x_coord = models.IntegerField(blank=True, null=True)
    y_coord = models.IntegerField(blank=True, null=True)
    zone = models.CharField(max_length=2, blank=True, null=True)
    
#a base storage model that will record all of the puck recovery data in the dataset
class Recoveries(models.Model):
    recovery_id = models.IntegerField(unique=True, primary_key=True)
    game_id = models.ForeignKey("Games", on_delete=models.CASCADE, related_name='recoveries')
    period = models.IntegerField(blank=True, null=True)
    periodtime = models.IntegerField(blank=True, null=True)
    gametime = models.IntegerField(blank=True, null=True)
    home_team_skaters = models.IntegerField(blank=True, null=True)
    away_team_skaters = models.IntegerField(blank=True, null=True)
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='recoveries')
    player_id = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='recoveries')
    x_coord = models.IntegerField(blank=True, null=True)
    y_coord = models.IntegerField(blank=True, null=True)
    zone = models.CharField(max_length=2, blank=True, null=True)
    
#a base storage model that will record all of the penalty data in the dataset
class Penalties(models.Model):
    
    class Meta:
        unique_together = (('penalty_id', 'team_id'))
    
    penalty_id = models.IntegerField()
    game_id = models.ForeignKey("Games", on_delete=models.CASCADE, related_name='penalties')
    period = models.IntegerField(blank=True, null=True)
    periodtime = models.IntegerField(blank=True, null=True)
    gametime = models.IntegerField(blank=True, null=True)
    home_team_skaters = models.IntegerField(blank=True, null=True)
    away_team_skaters = models.IntegerField(blank=True, null=True)
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, related_name='penalties')
    player_id = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='penalties')
    taken = models.BooleanField(blank=True, null=True) #true if took penalty, false if drew penalty
    infraction_type = models.CharField(max_length=50, blank=True, null=True)
    x_coord = models.IntegerField(blank=True, null=True)
    y_coord = models.IntegerField(blank=True, null=True)
    zone = models.CharField(max_length=2, blank=True, null=True)
    
#a base storage model that will record all of the faceoff data in the dataset
class Faceoffs(models.Model):
    
    class Meta:
        unique_together = (('faceoff_id', 'team_id'))
        
    faceoff_id = models.IntegerField(default=-1)
    game_id = models.ForeignKey("Games", on_delete=models.CASCADE, related_name='faceoffs')
    period = models.IntegerField(blank=True, null=True)
    periodtime = models.IntegerField(blank=True, null=True)
    gametime = models.IntegerField(blank=True, null=True)
    home_team_skaters = models.IntegerField(blank=True, null=True)
    away_team_skaters = models.IntegerField(blank=True, null=True)
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='faceoffs')
    player_id = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='faceoffs')
    success = models.BooleanField(blank=True, null=True) #true if won, false if lost
    x_coord = models.IntegerField(blank=True, null=True)
    y_coord = models.IntegerField(blank=True, null=True)
    zone = models.CharField(max_length=2, blank=True, null=True)
    
#a base storage model that will record all of the entry/exit data in the dataset
class EE(models.Model):
    ee_id = models.IntegerField(unique=True, primary_key=True)
    game_id = models.ForeignKey("Games", on_delete=models.CASCADE, related_name='ee')
    period = models.IntegerField(blank=True, null=True)
    periodtime = models.IntegerField(blank=True, null=True)
    gametime = models.IntegerField(blank=True, null=True)
    home_team_skaters = models.IntegerField(blank=True, null=True)
    away_team_skaters = models.IntegerField(blank=True, null=True)
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='ee')
    player_id = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='ee')
    defended_by_id = models.ForeignKey("Players", on_delete=models.CASCADE, blank=True, null=True, related_name='ee_defended')
    type_ee = models.CharField(max_length = 30,blank=True, null=True) #true if won, false if lost
    x_coord = models.IntegerField(blank=True, null=True)
    y_coord = models.IntegerField(blank=True, null=True)
    zone = models.CharField(max_length=2, blank=True, null=True)
    
    
 
############################################################################################# 



#an aggregation model that will summary game-to-game data per player
class PlayerGame(models.Model):
    pg_id = models.IntegerField(unique=True, primary_key=True)
    game_id = models.ForeignKey("Games", on_delete=models.CASCADE, related_name='playergame')
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='playergame')
    player_id = models.ForeignKey("Players", on_delete=models.CASCADE, related_name='playergame')
    state = models.CharField(max_length=2, blank=True, null=True)
    g = models.FloatField(blank=True, null=True)
    a = models.FloatField(blank=True, null=True)
    CF = models.FloatField(blank=True, null=True)
    total_passes = models.FloatField(blank=True, null=True)
    successful_passes = models.FloatField(blank=True, null=True)
    pass_completion = models.FloatField(blank=True, null=True)
    penalty_diff = models.FloatField(blank=True, null=True)
    oz_takeaway = models.FloatField(blank=True, null=True)
    dz_takeaway = models.FloatField(blank=True, null=True)
    oz_recovery = models.FloatField(blank=True, null=True)
    dz_recovery = models.FloatField(blank=True, null=True)
    fo_win_percent = models.FloatField(blank=True, null=True)
    nzfo_win_percent = models.FloatField(blank=True, null=True)
    dzfo_win_percent = models.FloatField(blank=True, null=True)
    ozfo_win_percent = models.FloatField(blank=True, null=True)
    fo_taken = models.IntegerField(blank=True, null=True)
    fo_successful = models.IntegerField(blank=True, null=True)
    nzfo_taken = models.IntegerField(blank=True, null=True)
    nzfo_successful = models.IntegerField(blank=True, null=True)
    ozfo_taken = models.IntegerField(blank=True, null=True)
    ozfo_successful = models.IntegerField(blank=True, null=True)
    dzfo_taken = models.IntegerField(blank=True, null=True)
    dzfo_successful = models.IntegerField(blank=True, null=True)
    cx_rate = models.FloatField(blank=True, null=True)
    ux_rate = models.FloatField(blank=True, null=True)
    fx_rate = models.FloatField(blank=True, null=True)
    cx = models.FloatField(blank=True, null=True)
    ux = models.FloatField(blank=True, null=True)
    fx = models.FloatField(blank=True, null=True)
    ce_rate = models.FloatField(blank=True, null=True)
    ue_rate = models.FloatField(blank=True, null=True)
    fe_rate = models.FloatField(blank=True, null=True)
    ce = models.FloatField(blank=True, null=True)
    ue = models.FloatField(blank=True, null=True)
    fe = models.FloatField(blank=True, null=True)
    shots_for = models.FloatField(blank=True, null=True)
    shooting_percent = models.FloatField(blank=True, null=True)
    
#an aggregation model that will summary whole tournament data per player
class PlayerTourney(models.Model):
    pt_id = models.IntegerField(unique=True, primary_key=True)
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, related_name='playertourney')
    player_id = models.ForeignKey("Players", on_delete=models.CASCADE, related_name='playertourney')
    state = models.CharField(max_length=2, blank=True, null=True)
    gp = models.IntegerField(blank=True, null=True)
    g_gp = models.FloatField(blank=True, null=True)
    g_gp_percentile = models.FloatField(blank=True, null=True)
    a_gp = models.FloatField(blank=True, null=True)
    a_gp_percentile = models.FloatField(blank=True, null=True)
    CF_gp = models.FloatField(blank=True, null=True)
    CF_gp_percentile = models.FloatField(blank=True, null=True)
    total_passes_gp = models.FloatField(blank=True, null=True)
    successful_passes_gp = models.FloatField(blank=True, null=True)
    pass_completion = models.FloatField(blank=True, null=True)
    pass_completion_percentile = models.FloatField(blank=True, null=True)
    penalty_diff_gp = models.FloatField(blank=True, null=True)
    penalty_diff_gp_percentile = models.FloatField(blank=True, null=True)
    oz_takeaway_gp = models.FloatField(blank=True, null=True)
    dz_takeaway_gp = models.FloatField(blank=True, null=True)
    oz_recovery_gp = models.FloatField(blank=True, null=True)
    dz_recovery_gp = models.FloatField(blank=True, null=True)
    fo_win_percent = models.FloatField(blank=True, null=True)
    fo_taken_gp = models.IntegerField(blank=True, null=True)
    nzfo_win_percent = models.FloatField(blank=True, null=True)
    dzfo_win_percent = models.FloatField(blank=True, null=True)
    ozfo_win_percent = models.FloatField(blank=True, null=True)
    fo_successful_gp = models.IntegerField(blank=True, null=True)
    nzfo_taken_gp = models.IntegerField(blank=True, null=True)
    nzfo_successful_gp = models.IntegerField(blank=True, null=True)
    ozfo_taken_gp = models.IntegerField(blank=True, null=True)
    ozfo_successful_gp = models.IntegerField(blank=True, null=True)
    dzfo_taken_gp = models.IntegerField(blank=True, null=True)
    dzfo_successful_gp = models.IntegerField(blank=True, null=True)
    cx_rate = models.FloatField(blank=True, null=True)
    cx_rate_percentile = models.FloatField(blank=True, null=True)
    ux_rate = models.FloatField(blank=True, null=True)
    fx_rate = models.FloatField(blank=True, null=True)
    cx_gp = models.FloatField(blank=True, null=True)
    ux_gp = models.FloatField(blank=True, null=True)
    fx_gp = models.FloatField(blank=True, null=True)
    ce_rate = models.FloatField(blank=True, null=True)
    ce_rate_percentile = models.FloatField(blank=True, null=True)
    ue_rate = models.FloatField(blank=True, null=True)
    fe_rate = models.FloatField(blank=True, null=True)
    ce_gp = models.FloatField(blank=True, null=True)
    ue_gp = models.FloatField(blank=True, null=True)
    fe_gp = models.FloatField(blank=True, null=True)
    shots_for_gp = models.FloatField(blank=True, null=True)
    shots_for_gp_percentile = models.FloatField(blank=True, null=True)
    shooting_percent = models.FloatField(blank=True, null=True)
    shooting_percent_percentile = models.FloatField(blank=True, null=True)
    
#an aggregation model that will summarize game-to-game data per team
class TeamGame(models.Model):
    tg_id = models.IntegerField(unique=True, primary_key=True)
    game_id = models.ForeignKey("Games", on_delete=models.CASCADE, related_name='teamgame')
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='teamgame')
    state = models.CharField(max_length=2, blank=True, null=True)
    gf = models.FloatField(blank=True, null=True)
    ga = models.FloatField(blank=True, null=True)
    gf_percent = models.FloatField(blank=True, null=True)
    CF = models.FloatField(blank=True, null=True)
    CA = models.FloatField(blank=True, null=True)
    CF_percent = models.FloatField(blank=True, null=True)
    shots_for = models.FloatField(blank=True, null=True)
    shots_against = models.FloatField(blank=True, null=True)
    shots_share = models.FloatField(blank=True, null=True)
    shooting_percent = models.FloatField(blank=True, null=True)
    FF = models.FloatField(blank=True, null=True)
    FA = models.FloatField(blank=True, null=True)
    FF_percent = models.FloatField(blank=True, null=True)
    cx_rate = models.FloatField(blank=True, null=True)
    ux_rate = models.FloatField(blank=True, null=True)
    fx_rate = models.FloatField(blank=True, null=True)
    cx = models.FloatField(blank=True, null=True)
    ux = models.FloatField(blank=True, null=True)
    fx = models.FloatField(blank=True, null=True)
    ce_rate = models.FloatField(blank=True, null=True)
    ue_rate = models.FloatField(blank=True, null=True)
    fe_rate = models.FloatField(blank=True, null=True)
    ce = models.FloatField(blank=True, null=True)
    ue = models.FloatField(blank=True, null=True)
    fe = models.FloatField(blank=True, null=True)
    ce_against = models.FloatField(blank=True, null=True)
    ue_against = models.FloatField(blank=True, null=True)
    fe_against = models.FloatField(blank=True, null=True)
    ce_against_rate = models.FloatField(blank=True, null=True)
    zone_denial_rate = models.FloatField(blank=True, null=True)
    fo_win_percent = models.FloatField(blank=True, null=True)
    nzfo_win_percent = models.FloatField(blank=True, null=True)
    dzfo_win_percent = models.FloatField(blank=True, null=True)
    ozfo_win_percent = models.FloatField(blank=True, null=True)
    fo_taken = models.IntegerField(blank=True, null=True)
    fo_successful = models.IntegerField(blank=True, null=True)
    nzfo_taken = models.IntegerField(blank=True, null=True)
    nzfo_successful = models.IntegerField(blank=True, null=True)
    ozfo_taken = models.IntegerField(blank=True, null=True)
    ozfo_successful = models.IntegerField(blank=True, null=True)
    dzfo_taken = models.IntegerField(blank=True, null=True)
    dzfo_successful = models.IntegerField(blank=True, null=True)
    pass_completion = models.FloatField(blank=True, null=True)
    total_passes = models.FloatField(blank=True, null=True)
    successful_passes = models.FloatField(blank=True, null=True)
    puck_recoveries_won = models.FloatField(blank=True, null=True)
    puck_recoveries_lost = models.FloatField(blank=True, null=True)
    penalty_diff = models.FloatField(blank=True, null=True)
    screened_shots = models.FloatField(blank=True, null=True)
    
    
#an aggregation model that will summarize whoel tournament data per team
class TeamTourney(models.Model):
    tt_id = models.IntegerField(unique=True, primary_key=True)
    team_id = models.ForeignKey("Teams", on_delete=models.CASCADE, blank=True, null=True, related_name='teamtourney')
    state = models.CharField(max_length=2, blank=True, null=True)
    gp = models.IntegerField(blank=True, null=True)
    gf_gp = models.FloatField(blank=True, null=True)
    ga_gp = models.FloatField(blank=True, null=True)
    gf_percent = models.FloatField(blank=True, null=True)
    CF_gp = models.FloatField(blank=True, null=True)
    CA_gp = models.FloatField(blank=True, null=True)
    CF_percent = models.FloatField(blank=True, null=True)
    shots_for_gp = models.FloatField(blank=True, null=True)
    shots_against_gp = models.FloatField(blank=True, null=True)
    shots_share_gp = models.FloatField(blank=True, null=True)
    shooting_percent = models.FloatField(blank=True, null=True)
    save_percentage = models.FloatField(blank=True, null=True)
    PDO = models.FloatField(blank=True, null=True)
    FF_gp = models.FloatField(blank=True, null=True)
    FA_gp = models.FloatField(blank=True, null=True)
    FF_percent = models.FloatField(blank=True, null=True)
    cx_rate = models.FloatField(blank=True, null=True)
    ux_rate = models.FloatField(blank=True, null=True)
    fx_rate = models.FloatField(blank=True, null=True)
    cx_gp = models.FloatField(blank=True, null=True)
    ux_gp = models.FloatField(blank=True, null=True)
    fx_gp = models.FloatField(blank=True, null=True)
    ce_rate = models.FloatField(blank=True, null=True)
    ue_rate = models.FloatField(blank=True, null=True)
    fe_rate = models.FloatField(blank=True, null=True)
    ce_gp = models.FloatField(blank=True, null=True)
    ue_gp = models.FloatField(blank=True, null=True)
    fe_gp = models.FloatField(blank=True, null=True)
    ce_against_gp = models.FloatField(blank=True, null=True)
    ue_against_gp = models.FloatField(blank=True, null=True)
    fe_against_gp = models.FloatField(blank=True, null=True)
    ce_against_rate = models.FloatField(blank=True, null=True)
    zone_denial_rate = models.FloatField(blank=True, null=True)
    fo_win_percent = models.FloatField(blank=True, null=True)
    nzfo_win_percent = models.FloatField(blank=True, null=True)
    dzfo_win_percent = models.FloatField(blank=True, null=True)
    ozfo_win_percent = models.FloatField(blank=True, null=True)
    fo_taken_gp = models.IntegerField(blank=True, null=True)
    fo_successful_gp = models.IntegerField(blank=True, null=True)
    nzfo_taken_gp = models.IntegerField(blank=True, null=True)
    nzfo_successful_gp = models.IntegerField(blank=True, null=True)
    ozfo_taken_gp = models.IntegerField(blank=True, null=True)
    ozfo_successful_gp = models.IntegerField(blank=True, null=True)
    dzfo_taken_gp = models.IntegerField(blank=True, null=True)
    dzfo_successful_gp = models.IntegerField(blank=True, null=True)
    pass_completion = models.FloatField(blank=True, null=True)
    total_passes_gp = models.FloatField(blank=True, null=True)
    successful_passes_gp = models.FloatField(blank=True, null=True)
    gf_gp_percentile = models.FloatField(blank=True, null=True)
    ga_gp_percentile = models.FloatField(blank=True, null=True)
    gf_percent_percentile = models.FloatField(blank=True, null=True)
    CF_gp_percentile = models.FloatField(blank=True, null=True)
    CA_gp_percentile = models.FloatField(blank=True, null=True)
    CF_percent_percentile = models.FloatField(blank=True, null=True)
    shots_for_gp_percentile = models.FloatField(blank=True, null=True)
    shots_against_gp_percentile = models.FloatField(blank=True, null=True)
    shots_share_gp_percentile = models.FloatField(blank=True, null=True)
    shooting_percent_percentile = models.FloatField(blank=True, null=True)
    save_percentage_percentile = models.FloatField(blank=True, null=True)
    PDO_percentile = models.FloatField(blank=True, null=True)
    FF_gp_percentile = models.FloatField(blank=True, null=True)
    FA_gp_percentile = models.FloatField(blank=True, null=True)
    FF_percent_percentile = models.FloatField(blank=True, null=True)
    cx_rate_percentile = models.FloatField(blank=True, null=True)
    ux_rate_percentile = models.FloatField(blank=True, null=True)
    fx_rate_percentile = models.FloatField(blank=True, null=True)
    cx_gp_percentile = models.FloatField(blank=True, null=True)
    ux_gp_percentile = models.FloatField(blank=True, null=True)
    fx_gp_percentile = models.FloatField(blank=True, null=True)
    ce_rate_percentile = models.FloatField(blank=True, null=True)
    ue_rate_percentile = models.FloatField(blank=True, null=True)
    fe_rate_percentile = models.FloatField(blank=True, null=True)
    ce_gp_percentile = models.FloatField(blank=True, null=True)
    ue_gp_percentile = models.FloatField(blank=True, null=True)
    fe_gp_percentile = models.FloatField(blank=True, null=True)
    ce_against_gp_percentile = models.FloatField(blank=True, null=True)
    ue_against_gp_percentile = models.FloatField(blank=True, null=True)
    fe_against_gp_percentile = models.FloatField(blank=True, null=True)
    ce_against_rate_percentile = models.FloatField(blank=True, null=True)
    zone_denial_rate_percentile = models.FloatField(blank=True, null=True)
    fo_win_percent_percentile = models.FloatField(blank=True, null=True)
    nzfo_win_percent_percentile = models.FloatField(blank=True, null=True)
    dzfo_win_percent_percentile = models.FloatField(blank=True, null=True)
    ozfo_win_percent_percentile = models.FloatField(blank=True, null=True)
    fo_taken_gp_percentile = models.IntegerField(blank=True, null=True)
    fo_successful_gp_percentile = models.IntegerField(blank=True, null=True)
    nzfo_taken_gp_percentile = models.IntegerField(blank=True, null=True)
    nzfo_successful_gp_percentile = models.IntegerField(blank=True, null=True)
    ozfo_taken_gp_percentile = models.IntegerField(blank=True, null=True)
    ozfo_successful_gp_percentile = models.IntegerField(blank=True, null=True)
    dzfo_taken_gp_percentile = models.IntegerField(blank=True, null=True)
    dzfo_successful_gp_percentile = models.IntegerField(blank=True, null=True)
    pass_completion_percentile = models.FloatField(blank=True, null=True)
    total_passes_gp_percentile = models.FloatField(blank=True, null=True)
    successful_passes_gp_percentile = models.FloatField(blank=True, null=True)

#easy use for bokeh
class BokehData(models.Model):
    Event = models.CharField(blank=True, null=True, max_length=100)
    Perspective = models.CharField(blank=True, null=True, max_length=100)
    Team = models.CharField(blank=True, null=True, max_length=100)
    Game = models.CharField(blank=True, null=True, max_length=100)
    Player = models.CharField(blank=True, null=True, max_length=100)
    State = models.CharField(blank=True, null=True, max_length=100)
    color = models.CharField(blank=True, null=True, max_length=100)
    shape = models.CharField(blank=True, null=True, max_length=100)
    Team = models.CharField(blank=True, null=True, max_length=100)
    Details = models.CharField(blank=True, null=True, max_length=100)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    x1 = models.FloatField(blank=True, null=True)
    x2 = models.FloatField(blank=True, null=True)
    y1 = models.FloatField(blank=True, null=True)
    y2 = models.FloatField(blank=True, null=True)
    