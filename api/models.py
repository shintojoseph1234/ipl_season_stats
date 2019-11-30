# django imports
from django.db import models


class Matches(models.Model):
    '''
    Model stores the details of all matches.
    '''

    season          = models.IntegerField()
    winner          = models.CharField(max_length=255)
    city            = models.CharField(max_length=255)
    venue           = models.CharField(max_length=255)
    toss_winner     = models.CharField(max_length=255)
    toss_decision   = models.CharField(max_length=255)
    win_by_runs     = models.IntegerField()
    win_by_wickets  = models.IntegerField()
    player_of_match = models.CharField(max_length=255)


class Deliveries(models.Model):
    '''
    Model that stores the details of each match
    '''
    match_id        = models.ForeignKey(Matches, on_delete=models.CASCADE)
    batsman         = models.CharField(max_length=255)
    fielder         = models.CharField(max_length=255)
    batsman_runs    = models.CharField(max_length=255)
    dismissal_kind  = models.CharField(max_length=255)
