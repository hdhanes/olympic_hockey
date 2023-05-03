"""calgary_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
from olympic import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.player_summary, name='player_summary'), #base page - summarizes players tournament stats in two tables
    re_path(r'^player_summary/', views.player_summary, name='player_summary'), #also at this link
    re_path(r'^team_summary/', views.team_summary, name='team_summary'), #team summary page
    re_path(r'^event_locations/', views.event_locations, name='event_locations'), #even locations bokeh app
    re_path(r'^player_cards/', views.player_cards, name='player_cards') #player cards
]
