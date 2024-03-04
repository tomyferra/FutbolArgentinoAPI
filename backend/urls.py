from django.urls import path, include
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'leaderboard', views.LeaderboardViewSet)
router.register(r'teams', views.TeamsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
