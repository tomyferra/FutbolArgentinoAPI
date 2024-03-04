from .models import Leaderboard, Teams
from rest_framework import serializers


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'
