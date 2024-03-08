from django.contrib import admin
# Register your models here.
from .models import Leaderboard, Teams


admin.site.register(Leaderboard)
admin.site.register(Teams)
