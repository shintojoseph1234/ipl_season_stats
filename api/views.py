# django imports
from django.shortcuts import render

# REST imports
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Matches

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

    from django.db.models import Count, Max

    season = int(season)

    # top 4 winner teams
    winnner_queryset = Matches.objects.filter(season=season
                                        ).values_list('winner'
                                        ).annotate(winner_count=Count('id')
                                        ).order_by('winner_count'
                                        ).reverse()[:4]

    winner_dict = dict(winnner_queryset)
    print (winner_dict)

    # Team with max number of tosses
    toss_winner_queryset = Matches.objects.filter(season=season
                                            ).values_list('toss_winner'
                                            ).annotate(toss_winner_count=Count('id')
                                            ).order_by('toss_winner_count'
                                            ).reverse()

    toss_winner_dict = dict(toss_winner_queryset[:1])
    print (toss_winner_dict)

    # which player won max player of match
    player_of_match_queryset = Matches.objects.filter(season=season
                                        ).values_list('player_of_match'
                                        ).annotate(player_of_match_count=Count('id')
                                        ).order_by('player_of_match_count'
                                        ).reverse()[:1]

    player_of_match_dict = dict(player_of_match_queryset)
    print (player_of_match_dict)

    # team won max matches in the whole season
    winner_team = max(winner_dict, key=winner_dict.get)
    print (winner_team)

    # location having most number of wins for top team
    location_queryset = Matches.objects.filter(season=season,
                                               winner=winner_team
                                               ).values_list('city', 'venue'
                                               ).annotate(city_count=Count('id')
                                               ).order_by('city_count'
                                               ).reverse()[:1]

    location_dict = {b+"-"+a:c for a,b,c in location_queryset}
    print (location_dict)

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
    print (bat_percentage)

    #
    # Team with max number of runs
    top_runs_queryset = Matches.objects.filter(season=season
                                            ).values_list('winner','win_by_runs'
                                            ).order_by('-win_by_runs')[:1]
    top_runs_dict = dict(top_runs_queryset)
    print (top_runs_dict)

    # location having most number of matches
    location_most_queryset = Matches.objects.filter(season=season,
                                               ).values_list('city', 'venue'
                                               ).annotate(city_count=Count('id')
                                               ).order_by('city_count'
                                               )
                                            #    .reverse()[:1]

    print (location_most_queryset)

    # response message
    success = [{
            	"status": "success",
            	"data": {
            		"ingestion": 'ingestion_status',
                    "message"  : "message"
            	},
            }]

    return Response(success, status=status.HTTP_200_OK)
