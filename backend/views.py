from django.shortcuts import render
from rest_framework import viewsets
from .models import Leaderboard, Teams
from .serializers import LeaderboardSerializer, TeamSerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
