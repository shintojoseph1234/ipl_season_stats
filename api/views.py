# django imports
from django.shortcuts import render
from django.db.models import Count

# REST imports
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# local imports
from api.models import Matches
from api.plots import bar_graph_data_cleaner, pie_graph_data_cleaner, bar_graph, pie_graph

# other imports
import pandas as pd
import os

# index page function
def index(request):

    try:
        # find the years of IPL season
        seasons_queryset = Matches.objects.order_by('season').values_list('season', flat=True).distinct()
    except:
        # if not found return empty
        seasons_queryset = []

    # returns index.html template along with seasons
    return render(request, 'index.html', {'seasons':seasons_queryset})



@api_view(['GET'])
def ingest_csv(request):

    # current path
    current_path = os.getcwd()
    # matches csv file path
    matches_csv_path = current_path+"/media/csv/matches.csv"
    # deliveries csv file path
    deliveries_csv_path = current_path+"/media/csv/deliveries.csv"
    # read matches csv file
    matches_df = pd.read_csv(matches_csv_path)
    # read deliveries csv file
    deliveries_df = pd.read_csv(deliveries_csv_path)

    for index, row in matches_df.iterrows():
        print(row['id'], row['season'])

        try:
            match = Matches(season          = row['season'],
                            winner          = row['winner'],
                            city            = row['city'],
                            venue           = row['venue'],
                            toss_winner     = row['toss_winner'],
                            toss_decision   = row['toss_decision'],
                            win_by_runs     = row['win_by_runs'],
                            win_by_wickets  = row['win_by_wickets'],
                            player_of_match = row['player_of_match'],
                        )

            match.save()

            message          = "successfullyy ingested csv data"
            ingestion_status = "success"

        except:
            message          = "There was a problem with index "+str(index)
            ingestion_status = "failure"

    # response message
    success = [{
            	"status": "success",
            	"data": {
            		"ingestion": ingestion_status,
                    "message"  : message
            	},
            }]

    return Response(success, status=status.HTTP_200_OK)



@api_view(['GET'])
def season_stats(request, season):
    '''
    API endpoint that returns statics details
    for the input season.

    Parameters:
        season (str)   : Input season to find the stat details.

    Returns:
        list: returns
    '''

    # convert into integer
    season = int(season)

    # top 4 winner teams
    winnner_queryset = Matches.objects.filter(season=season
                                        ).values_list('winner'
                                        ).annotate(winner_count=Count('id')
                                        ).order_by('winner_count'
                                        ).reverse()[:4]
    # convert quertset to dict
    winner_dict = dict(winnner_queryset)
    # clean the data to plot bar graph
    x,y,colors = bar_graph_data_cleaner(winner_dict)
    # heading
    heading = ''
    # plotted html div of bar graph
    winner_bar_div = bar_graph(x,y,heading,colors)


    # Team with max number of tosses
    toss_winner_queryset = Matches.objects.filter(season=season
                                            ).values_list('toss_winner'
                                            ).annotate(toss_winner_count=Count('id')
                                            ).order_by('toss_winner_count'
                                            ).reverse()

    # convert quertset to dict
    toss_winner_dict = dict(toss_winner_queryset[:1])

    # which player won max player of match
    player_of_match_queryset = Matches.objects.filter(season=season
                                        ).values_list('player_of_match'
                                        ).annotate(player_of_match_count=Count('id')
                                        ).order_by('player_of_match_count'
                                        ).reverse()[:1]

    player_of_match_dict = dict(player_of_match_queryset)

    # team won max matches in the whole season
    winner_team = max(winner_dict, key=winner_dict.get)

    # location having most number of wins for top team
    location_queryset = Matches.objects.filter(season=season,
                                               winner=winner_team
                                               ).values_list('city', 'venue'
                                               ).annotate(city_count=Count('id')
                                               ).order_by('city_count'
                                               ).reverse()[:1]
    # combine location names
    location_dict = {b+"-"+a:c for a,b,c in location_queryset}

    # list of toss winners
    toss_winner_list = list(dict(toss_winner_queryset).keys())
    # get the toss winners count
    all_toss_winner_queryset = Matches.objects.filter(season=season,
                                                  toss_winner__in=toss_winner_list,
                                                  ).values("toss_decision"
                                                  ).annotate(Count('toss_decision'))

    # convert quertset to this format {"bat":26, "field":"32"}
    toss_dict = {each_toss['toss_decision']:each_toss['toss_decision__count']
                                        for each_toss in all_toss_winner_queryset}

    # sum the values to find total
    total = sum(toss_dict.values())
    # find the bat percentage
    bat_percentage = (toss_dict['bat']/total)*100
    # input to pie graph
    pie_graph_data = {"BAT":round(bat_percentage,2), "FIELD":round(100-bat_percentage,2)}
    # pie data inputs
    labels,values,colors = pie_graph_data_cleaner(pie_graph_data)
    # pie data plotted as html div
    pie_div = pie_graph(labels,values,colors)

    # Team with max number of runs
    top_runs_queryset = Matches.objects.filter(season=season
                                            ).values_list('winner','win_by_runs'
                                            ).order_by('-win_by_runs')[:1]
    top_runs_dict = dict(top_runs_queryset)

    # location having most number of matches
    location_most_queryset = Matches.objects.filter(season=season,
                                               ).values_list('city', 'venue'
                                               ).annotate(city_count=Count('id')
                                               ).order_by('city_count'
                                               )


    # response message
    success = [{
            	"status": "success",
            	"data": {
                    "top_4_winner"          : winner_dict,
                    "max_toss__win_team"    : toss_winner_dict,
                    "max_player_of_match"   : player_of_match_dict,
                    "max_winner_team"       : winner_team,
                    "top_runs_team"         :top_runs_dict,
                    "max_win_location"      :location_dict,
                    "top_4_winner_bar_div"  : winner_bar_div,
                    "pie_div"               :pie_div,


            	},
            }]

    return Response(success, status=status.HTTP_200_OK)
