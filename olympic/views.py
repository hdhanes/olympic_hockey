from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from olympic.models import PlayerTourney, Teams, TeamTourney, Shots, Passes, Takeaways, Recoveries, Penalties, Faceoffs, EE, Players, Games
from django.db.models import Q
import numpy as np
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS, Select, Slider, Select, MultiSelect, MultiChoice, IndexFilter, CDSView, OpenHead, Arrow
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.core.properties import value
from bokeh.events import DocumentReady
from bokeh.util.hex import hexbin
from bokeh.transform import linear_cmap
from bokeh.palettes import Inferno



# Create your views here.
def player_summary(request):
    """Get PlayerTourney and uses the data for F/D Summary pages

    Args:
        request (_type_): web request

    Returns:
        _type_: rendered HTTPResponse
    """
    context_dict = {}
    
    #team filter
    context_dict['curr_team'] = 'Canada'
    if 'team' in request.GET:
        if request.GET["team"]:
            try:
                context_dict['curr_team'] = request.GET['team']
            except ValueError as e:
                print(e)
    context_dict['all_teams'] = ['All', 'Canada', 'Finland', 'ROC',
                 'United States']
    print(context_dict['curr_team'])
    
    #state filter
    context_dict['curr_state'] = 'ES'
    if 'state' in request.GET:
        if request.GET['state']:
            try:
                context_dict['curr_state'] = request.GET['state']
            except ValueError as e:
                print(e)
    context_dict['all_states'] = ['All', 'ES', 'PP', 'PK']
    
    #query data
    if context_dict['curr_team'] != 'All':
        current_team_obj = Teams.objects.filter(name=context_dict['curr_team'])[0]
        context_dict['all_pt'] = PlayerTourney.objects.filter(Q(state=context_dict['curr_state']) & Q(team_id=current_team_obj)).order_by("-CF_gp")
    else:
        context_dict['all_pt'] = PlayerTourney.objects.filter(Q(state=context_dict['curr_state'])).order_by("-CF_gp")
    
    #add for points
    for pt in context_dict['all_pt']:
        pt.p_gp = round(pt.a_gp + pt.g_gp,1)
    
    return render(request, 'olympic/player_summary.html', context=context_dict)







def team_summary(request):
    """Get TeamTourney and uses the data for team summary table
    
    Args:
        request (_type_): web request

    Returns:
        _type_: rendered HTTPResponse
    """
    context_dict = {}
    
    #display filter
    context_dict['curr_display'] = 'Real'
    if 'display' in request.GET:
        if request.GET["display"]:
            try:
                context_dict['curr_display'] = request.GET['display']
            except ValueError as e:
                print(e)
    context_dict['all_displays'] = ['Real', 'Rank']
    
    #state filter
    context_dict['curr_state'] = 'ES'
    if 'state' in request.GET:
        if request.GET['state']:
            try:
                context_dict['curr_state'] = request.GET['state']
            except ValueError as e:
                print(e)
    context_dict['all_states'] = ['All', 'ES', 'PP', 'PK']
    
    #data filter
    context_dict['curr_data'] = 'Box Score'
    if 'data' in request.GET:
        if request.GET['data']:
            try:
                context_dict['curr_data'] = request.GET['data']
            except ValueError as e:
                print(e)
    context_dict['all_data'] = ['Box Score', 'Transition', 'Faceoffs', 'Advanced']
    
    #query data
    print(context_dict['curr_data'], context_dict['curr_display'], context_dict['curr_state'])
    context_dict['all_tt'] = TeamTourney.objects.filter(Q(state=context_dict['curr_state'])).order_by("-gp")
    
    #iterate and assign colors if display==Rank
    field_list = TeamTourney._meta.get_fields()
    for tt in context_dict['all_tt']:
        for f in field_list:
            q = f.name
            if 'percentile' in q:
                if getattr(tt, q) == 1:
                    setattr(tt,q+'_color', '#78a8f5')
                elif getattr(tt, q) == 2:
                    setattr(tt,q+'_color', '#aec9f5')
                elif getattr(tt, q) == 3:
                    setattr(tt,q+'_color', '#d7e3f5')
                else:
                    setattr(tt,q+'_color', '#f5ded7')
            else:
                setattr(tt,q+'_color', '#FFFFFF')
                
    
    return render(request, 'olympic/team_summary.html', context=context_dict)











def event_locations(request):
    """Get all Event models and create an interactive bokeh application to go over the data spatially
    
    Args:
        request (_type_): web request

    Returns:
        _type_: rendered HTTPResponse (bokeh framework)
    """
    context_dict = {}
    
    #query all shots
    event_list_dict = []
    
    print("begin query")
    all_shots = Shots.objects.all()
    for s in all_shots:
        
        #shots for
        d = {}
        d['Event'] = 'Shots'
        d['Perspective'] = 'For'
        d['Team'] = s.team_id.name
        d['Game'] = str(s.game_id.game_id)
        d['Player'] = s.player_id.name
        if s.home_team_skaters == s.away_team_skaters:
            d['State'] = 'ES'
        elif (s.home_team_skaters > s.away_team_skaters):
            if (s.team_id.name == s.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (s.team_id.name == s.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if s.result == 'Goal':
            d['color'] = 'Green'
        elif s.result == 'On Net':
            d['color'] = 'Blue'
        elif s.result == 'Missed':
            d['color'] = 'Orange'
        else:
            d['color'] = 'Red'
        d['shape'] = 'circle'
        d['x'] = s.x_coord
        d['y'] = s.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = s.result + (f", {s.shot_type}" if len(s.shot_type) > 0 else "") + (", traffic" if s.traffic == 'True' else "") + (", one-timer" if s.one_timer == 'True' else "")
        event_list_dict.append(d)
                
        #shots against
        d = {}
        d['Event'] = 'Shots'
        d['Perspective'] = 'Against'
        if s.team_id.name == s.game_id.home_team.name:
            d['Team'] = s.game_id.away_team.name
        else:
            d['Team'] = s.game_id.home_team.name
        d['Game'] = str(s.game_id.game_id)
        d['Player'] = s.player_id.name
        if s.home_team_skaters == s.away_team_skaters:
            d['State'] = 'ES'
        elif (s.home_team_skaters > s.away_team_skaters):
            if (d['Team'] == s.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (d['Team'] == s.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if s.result == 'Goal':
            d['color'] = 'Green'
        elif s.result == 'On Net':
            d['color'] = 'Blue'
        elif s.result == 'Missed':
            d['color'] = 'Orange'
        else:
            d['color'] = 'Red'
        d['shape'] = 'square'
        d['x'] = 200-s.x_coord
        d['y'] = 85-s.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = s.result + (f", {s.shot_type}" if len(s.shot_type) > 0 else "") + (", traffic" if s.traffic == 'True' else "") + (", one-timer" if s.one_timer == 'True' else "")
        event_list_dict.append(d)
        
    print("done shots")

        
    #query all passes
    all_passes = Passes.objects.all()
    for p in all_passes:
        
        #passes for
        d = {}
        d['Event'] = 'Passes'
        d['Perspective'] = 'For'
        d['Team'] = p.team_id.name
        d['Game'] = str(p.game_id.game_id)
        d['Player'] = p.passer_id.name
        if p.home_team_skaters == p.away_team_skaters:
            d['State'] = 'ES'
        elif (p.home_team_skaters > p.away_team_skaters):
            if (p.team_id.name == p.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (p.team_id.name == p.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if p.success == True:
            d['color'] = 'Green'
        else:
            d['color'] = 'Red'
        d['shape'] = 'circle'
        d['x'] = p.passer_x_coord
        d['y'] = p.passer_y_coord
        d['x1'] = p.passer_x_coord
        d['y1'] = p.passer_y_coord
        d['x2'] = p.receiver_x_coord
        d['y2'] = p.receiver_y_coord
        d['Details'] = ('Play' if p.success else 'Incomplete play') + ', ' + p.pass_type + ', receiver: ' + p.receiver_id.name
        event_list_dict.append(d)
        
        #passes against
        d = {}
        d['Event'] = 'Passes'
        d['Perspective'] = 'Against'
        if p.team_id.name == p.game_id.home_team.name:
            d['Team'] = p.game_id.away_team.name
        else:
            d['Team'] = p.game_id.home_team.name
        d['Game'] = str(p.game_id.game_id)
        d['Player'] = p.passer_id.name
        if p.home_team_skaters == p.away_team_skaters:
            d['State'] = 'ES'
        elif (p.home_team_skaters > p.away_team_skaters):
            if (p.team_id.name == p.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (p.team_id.name == p.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if p.success == True:
            d['color'] = 'Green'
        else:
            d['color'] = 'Red'
        d['shape'] = 'square'
        d['x'] = 200-p.passer_x_coord
        d['y'] = 85-p.passer_y_coord
        d['x1'] = 200-p.passer_x_coord
        d['y1'] = 85-p.passer_y_coord
        d['x2'] = 200-p.receiver_x_coord
        d['y2'] = 85-p.receiver_y_coord
        d['Details'] = ('Play' if p.success else 'Incomplete play') + ', ' + p.pass_type + ', receiver: ' + p.receiver_id.name
        event_list_dict.append(d)
        
    print("done passes")
        
    #query all takeaways
    all_takes = Takeaways.objects.all()
    for t in all_takes:
        
        #takeaways for
        d = {}
        d['Event'] = 'Takeaways'
        d['Perspective'] = 'For'
        d['Team'] = t.team_id.name
        d['Game'] = str(t.game_id.game_id)
        d['Player'] = t.player_id.name
        if t.home_team_skaters == t.away_team_skaters:
            d['State'] = 'ES'
        elif (t.home_team_skaters > t.away_team_skaters):
            if (t.team_id.name == t.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (t.team_id.name == t.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        d['color'] = 'Green'
        d['shape'] = 'circle'
        d['x'] = t.x_coord
        d['y'] = t.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = ('nz' if t.zone == 'nz' else ('oz' if t.zone != 'oz' else 'dz'))
        event_list_dict.append(d)
        
        #passes against
        d = {}
        d['Event'] = 'Takeaways'
        d['Perspective'] = 'Against'
        if t.team_id.name == t.game_id.home_team.name:
            d['Team'] = t.game_id.away_team.name
        else:
            d['Team'] = t.game_id.home_team.name
        d['Game'] = str(t.game_id.game_id)
        d['Player'] = t.player_id.name
        if t.home_team_skaters == t.away_team_skaters:
            d['State'] = 'ES'
        elif (t.home_team_skaters > t.away_team_skaters):
            if (t.team_id.name == t.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (t.team_id.name == t.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        d['color'] = 'Red'
        d['shape'] = 'square'
        d['x'] = 200-t.x_coord
        d['y'] = 85-t.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = ('nz' if t.zone == 'nz' else ('oz' if t.zone != 'oz' else 'dz'))
        event_list_dict.append(d)
        
    print("done takeaways")
        
    #query all recoveries
    all_recov = Recoveries.objects.all()
    for r in all_recov:
        
        #takeaways for
        d = {}
        d['Event'] = 'Recoveries'
        d['Perspective'] = 'For'
        d['Team'] = r.team_id.name
        d['Game'] = str(r.game_id.game_id)
        d['Player'] = r.player_id.name
        if r.home_team_skaters == r.away_team_skaters:
            d['State'] = 'ES'
        elif (r.home_team_skaters > r.away_team_skaters):
            if (r.team_id.name == r.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (r.team_id.name == r.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        d['color'] = 'Green'
        d['shape'] = 'circle'
        d['x'] = r.x_coord
        d['y'] = r.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = ('nz' if r.zone == 'nz' else ('oz' if r.zone != 'oz' else 'dz'))
        event_list_dict.append(d)
        
        #passes against
        d = {}
        d['Event'] = 'Recoveries'
        d['Perspective'] = 'Against'
        if r.team_id.name == r.game_id.home_team.name:
            d['Team'] = r.game_id.away_team.name
        else:
            d['Team'] = r.game_id.home_team.name
        d['Game'] = str(r.game_id.game_id)
        d['Player'] = r.player_id.name
        if r.home_team_skaters == r.away_team_skaters:
            d['State'] = 'ES'
        elif (r.home_team_skaters > r.away_team_skaters):
            if (r.team_id.name == r.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (r.team_id.name == r.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        d['color'] = 'Red'
        d['shape'] = 'square'
        d['x'] = 200-r.x_coord
        d['y'] = 85-r.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = ('nz' if r.zone == 'nz' else ('oz' if r.zone != 'oz' else 'dz'))
        event_list_dict.append(d)
        
    print("done recoveries")
        
    #query all penalties
    all_pen = Penalties.objects.all()
    for r in all_pen:
        
        #pens for
        d = {}
        d['Event'] = 'Penalties'
        d['Perspective'] = 'For'
        d['Team'] = r.team_id.name
        d['Game'] = str(r.game_id.game_id)
        try:
            d['Player'] = r.player_id.name
        except:
            d['Player'] = ''
        if r.home_team_skaters == r.away_team_skaters:
            d['State'] = 'ES'
        elif (r.home_team_skaters > r.away_team_skaters):
            if (r.team_id.name == r.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (r.team_id.name == r.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if r.taken == True:
            d['color'] = 'Red'
        else:
            d['color'] = 'Green'
        d['shape'] = 'circle'
        d['x'] = r.x_coord
        d['y'] = r.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = ('Taken' if r.taken else 'Drawn') + ', ' + r.infraction_type
        event_list_dict.append(d)
        
        #pens against
        d = {}
        d['Event'] = 'Penalties'
        d['Perspective'] = 'Against'
        if r.team_id.name == r.game_id.home_team.name:
            d['Team'] = r.game_id.away_team.name
        else:
            d['Team'] = r.game_id.home_team.name
        d['Game'] = str(r.game_id.game_id)
        try:
            d['Player'] = r.player_id.name
        except:
            d['Player'] = ''
        if r.home_team_skaters == r.away_team_skaters:
            d['State'] = 'ES'
        elif (r.home_team_skaters > r.away_team_skaters):
            if (r.team_id.name == r.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (r.team_id.name == r.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if r.taken == True:
            d['color'] = 'Red'
        else:
            d['color'] = 'Green'
        d['shape'] = 'square'
        d['x'] = 200-r.x_coord
        d['y'] = 85-r.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = ('Drawn' if r.taken else 'Taken') + ', ' + r.infraction_type
        event_list_dict.append(d)
        
    print("done penalties")
        
    #query all faceoffs
    all_f = Faceoffs.objects.all()
    for r in all_f:
        
        #pens for
        d = {}
        d['Event'] = 'Faceoffs'
        d['Perspective'] = 'For'
        d['Team'] = r.team_id.name
        d['Game'] = str(r.game_id.game_id)
        d['Player'] = r.player_id.name
        if r.home_team_skaters == r.away_team_skaters:
            d['State'] = 'ES'
        elif (r.home_team_skaters > r.away_team_skaters):
            if (r.team_id.name == r.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (r.team_id.name == r.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if r.success == True:
            d['color'] = 'Green'
        else:
            d['color'] = 'Red'
        d['shape'] = 'circle'
        d['x'] = r.x_coord
        d['y'] = r.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = ('Won' if r.success else 'Lost') + ', ' + r.zone
        event_list_dict.append(d)
        
        #pens against
        d = {}
        d['Event'] = 'Faceoffs'
        d['Perspective'] = 'Against'
        if r.team_id.name == r.game_id.home_team.name:
            d['Team'] = r.game_id.away_team.name
        else:
            d['Team'] = r.game_id.home_team.name
        d['Game'] = str(r.game_id.game_id)
        d['Player'] = r.player_id.name
        if r.home_team_skaters == r.away_team_skaters:
            d['State'] = 'ES'
        elif (r.home_team_skaters > r.away_team_skaters):
            if (r.team_id.name == r.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (r.team_id.name == r.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if r.success == True:
            d['color'] = 'Green'
        else:
            d['color'] = 'Red'
        d['shape'] = 'square'
        d['x'] = 200-r.x_coord
        d['y'] = 85-r.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        d['Details'] = ('Won' if r.success else 'Lost') + ', ' + r.zone
        event_list_dict.append(d)
        
    print("done faceoffs")
        
    all_ee = EE.objects.all()
    for s in all_ee:
        
        #shots for
        d = {}
        d['Event'] = 'EE'
        d['Perspective'] = 'For'
        d['Team'] = s.team_id.name
        d['Game'] = str(s.game_id.game_id)
        d['Player'] = s.player_id.name
        if s.home_team_skaters == s.away_team_skaters:
            d['State'] = 'ES'
        elif (s.home_team_skaters > s.away_team_skaters):
            if (s.team_id.name == s.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (s.team_id.name == s.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if s.type_ee == 'cx' or s.type_ee == 'ce':
            d['color'] = 'Green'
        elif s.type_ee == 'ux' or s.type_ee == 'ue':
            d['color'] = 'Orange'
        else:
            d['color'] = 'Red'
        if s.type_ee.endswith("x"):
            d['shape'] = 'circle'
        else:
            d['shape'] = 'square'
        d['x'] = s.x_coord
        d['y'] = s.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        try:
            d['Details'] = s.type_ee + f', {s.defended_by_id.name}'   
        except:
            d['Details'] = s.type_ee 
        event_list_dict.append(d)
        
        #shots against
        d = {}
        d['Event'] = 'EE'
        d['Perspective'] = 'Against'
        if s.team_id.name == s.game_id.home_team.name:
            d['Team'] = s.game_id.away_team.name
        else:
            d['Team'] = s.game_id.home_team.name
        d['Game'] = str(s.game_id.game_id)
        d['Player'] = s.player_id.name
        if s.home_team_skaters == s.away_team_skaters:
            d['State'] = 'ES'
        elif (s.home_team_skaters > s.away_team_skaters):
            if (d['Team'] == s.game_id.home_team.name):
                d['State'] = 'PP'
            else:
                d['State'] = 'PK'
        else:
            if (d['Team'] == s.game_id.away_team.name):
                d['State'] = 'PK'
            else:
                d['State'] = 'PP'
        if s.type_ee == 'cx' or s.type_ee == 'ce':
            d['color'] = 'Green'
        elif s.type_ee == 'ux' or s.type_ee == 'ue':
            d['color'] = 'Orange'
        else:
            d['color'] = 'Red'
        if s.type_ee.endswith("x"):
            d['shape'] = 'circle'
        else:
            d['shape'] = 'square'
        d['shape'] = 'square'
        d['x'] = 200-s.x_coord
        d['y'] = 85-s.y_coord
        d['x1'] = -100
        d['y1'] = -100
        d['x2'] = -100
        d['y2'] = -100
        try:
            d['Details'] = s.type_ee + f', {s.defended_by_id.name}'   
        except:
            d['Details'] = s.type_ee         
        event_list_dict.append(d)
        
    print("done ee")
        
    #create dataframe and data source
    df = pd.DataFrame(event_list_dict)
    source = ColumnDataSource(df)
    
    #get all shots for
    idx = []
    for i, p in enumerate(event_list_dict):
        if p['Event'] == 'Shots' and p['Perspective'] == 'For':
            idx.append(i)
    
    #create the tooltips
    tooltips = [
        ('Event', '@Event'),
        ('Team', '@Team'),
        ('Player', '@Player'),
        ('State', '@State'),
        ('Perspective', '@Perspective'),
        ('Details', '@Details'),
    ]        
    
    #inputs
    events = Select(title="Event:", value="Shots", options=['Shots', 'Passes', 'Takeaways', 'Recoveries', 
                                                            'Penalties', 'Faceoffs', 'EE'])
    teams = MultiSelect(title="Teams:", value=['Canada', 'Finland', 'ROC', 'United States'], options=['Canada', 'Finland','ROC','United States'])
    players = MultiChoice(title="Players:", value=[], options=list(Players.objects.values_list("name", flat=True)))
    vals = list(Games.objects.values_list("game_id", flat=True))
    vals = sorted([str(x) for x in vals])
    games = MultiSelect(title="Games:", value=vals, options=vals)
    state = Select(title="State:", value='All', options=['All','ES', 'PP', 'PK'])
    perspective = Select(title="Perspective:", value='For', options=['For', 'Against'])
    colors = MultiSelect(title="Types:", value=['Green','Blue','Orange','Red'], options=['Green','Blue','Orange','Red'])
    
    #graph
    p = figure(height=510, title="", toolbar_location=None, tooltips=tooltips, width=1200,
               x_range=(-5,205), y_range=(-5,90))
    p.grid.visible = False
    
    print("graph plotted")
    
    #callbacks
    filter = IndexFilter(indices=idx)
    callback_events = CustomJS(args=dict(src=source, filter=filter, event=events, state=state, per=perspective, teams=teams, games=games, players=players, cols=colors), code='''
                               const indices = [];
                                for (var i = 0; i < src.get_length(); i++) {
                                    const team_list = teams.value;
                                    const game_list = games.value;
                                    const players_list = players.value;
                                    const colors_list = cols.value;
                                    console.log(colors_list)
                                    if (players_list.length !=0){
                                         if (state.value != 'All'){
                                        if ((src.data['Event'][i] == event.value) && (src.data['State'][i] == state.value) && (src.data['Perspective'][i] == per.value) && (team_list.includes(src.data['Team'][i])) && (game_list.includes(src.data['Game'][i])) && (players_list.includes(src.data['Player'][i])) && (colors_list.includes(src.data['color'][i]))){
                                            indices.push(i);
                                        }
                                    } else {
                                       if ((src.data['Event'][i] == event.value) && (src.data['Perspective'][i] == per.value) && (team_list.includes(src.data['Team'][i])) && (game_list.includes(src.data['Game'][i])) && (players_list.includes(src.data['Player'][i])) && (colors_list.includes(src.data['color'][i]))){
                                            indices.push(i);
                                        } 
                                    }
                                        
                                    } else {
                                        
                                         if (state.value != 'All'){
                                        if ((src.data['Event'][i] == event.value) && (src.data['State'][i] == state.value) && (src.data['Perspective'][i] == per.value) && (team_list.includes(src.data['Team'][i])) && (game_list.includes(src.data['Game'][i])) && (colors_list.includes(src.data['color'][i]))){
                                            indices.push(i);
                                        }
                                    } else {
                                       if ((src.data['Event'][i] == event.value) && (src.data['Perspective'][i] == per.value) && (team_list.includes(src.data['Team'][i])) && (game_list.includes(src.data['Game'][i])) && (colors_list.includes(src.data['color'][i]))){
                                            indices.push(i);
                                        } 
                                    }
                                        
                                    }
                                    
                                   
                                }
                                filter.indices = indices;                                
                                src.change.emit();
                                ''')
    
    
    events.js_on_change('value', callback_events)
    state.js_on_change('value', callback_events)
    perspective.js_on_change('value', callback_events)
    teams.js_on_change('value', callback_events)
    games.js_on_change('value', callback_events)
    players.js_on_change('value', callback_events)
    colors.js_on_change('value', callback_events)
    view = CDSView(source=source, filters=[filter])
    
    p.image_url( url=["https://o.quizlet.com/NZ6-sAVDg0KdopEd-jlW4Q_b.png"],
             x=1, y=1, w=200, h=85, anchor="bottom_left")
    p.scatter(x='x', y='y', source=source, size=12, color='color', fill_alpha=0.5, marker='shape', view=view)
    p.segment(x0='x1', y0='y1', x1='x2', y1='y2', color='color', source=source, view=view, line_cap='square')
    
    controls = [events, teams, players, games, state, perspective, colors]
    inputs = column(*controls, width=275, height=490)
    layout = row(inputs, p)
                
    event_script, event_div = components(layout, CDN)
    print(event_script)
    print(event_div)
    context_dict['event_script'] = event_script
    context_dict['event_div'] = event_div
    
    return render(request, 'olympic/event_locations.html', context=context_dict)










def player_cards(request):
    """Get PlayerTourney and uses it to create a percentile based "player card"

    Args:
        request (_type_): web request

    Returns:
        _type_: rendered HTTPResponse
    """
    
    all_pt = PlayerTourney.objects.filter(state='ES').order_by('team_id__team_id','player_id__name')
    
    
    #add special team shots
    added_spec = []
    for p in all_pt:
        p.pp_percentile = list(PlayerTourney.objects.filter(Q(player_id__name=p.player_id.name) & Q(state='PP')).values_list('shots_for_gp_percentile', flat=True))[0]
        p.pk_percentile = list(PlayerTourney.objects.filter(Q(player_id__name=p.player_id.name) & Q(state='PK')).values_list('shots_for_gp_percentile', flat=True))[0]
        added_spec.append(p)
    
    #add colors
    added_cols = []
    name_string = ''
    for p in added_spec:
        for f in ['CF_gp_percentile','g_gp_percentile','a_gp_percentile','pp_percentile','pk_percentile',
                  "shooting_percent_percentile", "pass_completion_percentile", 'cx_rate_percentile', 'ce_rate_percentile']:
            val = getattr(p,f)
            if val <= 0.4:
                col = '#f5b19d'
            elif val <= 0.5:
                col = '#f5ded7'
            elif val <= 0.6:
                col = '#d7e3f5'
            elif val <= 0.7:
                col = '#aec9f5'
            elif val <= 0.85:
                col = '#78a8f5'
            else:
                col = '#4287f5'
            setattr(p,f+'_col',col)
            setattr(p,'concat_name',p.player_id.name.replace(" ", ""))
        added_cols.append(p)
        name_string = name_string + '#' + p.concat_name + ', '
    all_pt = added_cols  
    name_string = name_string[:-2]  
    print(name_string)
    
    return render(request, 'olympic/player_cards.html', context={"all_pt":all_pt,
                                                                 'name_string':name_string})