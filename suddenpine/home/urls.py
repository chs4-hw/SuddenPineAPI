from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('api/home/housedetails', views.HouseDetailsView, 'HouseDetails')
router.register('api/home/housestats', views.HouseStatsView)
router.register('api/home/weeklogs', views.WeeklyLogsView)
router.register('api/home/roomstats', views.RoomStatsView)
router.register('api/home/devices', views.DevicesView)
router.register('api/home/roomcontrol', views.RoomControlView)
router.register('api/home/league', views.LeagueView)

urlpatterns = router.urls