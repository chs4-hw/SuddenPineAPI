from django.shortcuts import render
from .models import HouseDetails, HouseStats, WeeklyLogs, RoomStats, Devices, RoomControl, League
from rest_framework import viewsets, permissions, filters
from .serializers import HouseDetailsSerializer, HouseStatsSerializer, WeeklyLogsSerializer, RoomStatsSerializer, DevicesSerializer, RoomControlSerializer, LeagueSerializer

# Create your views here.

class HouseDetailsView(viewsets.ModelViewSet):
    #queryset = HouseDetails.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = HouseDetailsSerializer

    def get_queryset(self):
        return self.request.user.house.all()

    def perform_create(self, serializer):
        serializer.save(resident=self.request.user)    
   

class HouseStatsView(viewsets.ModelViewSet):
    queryset = HouseStats.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HouseStatsSerializer
    filter_backends = [
        filters.SearchFilter
    ]
    search_fields = ['house__id']

class WeeklyLogsView(viewsets.ModelViewSet):
    queryset = WeeklyLogs.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WeeklyLogsSerializer

class RoomStatsView(viewsets.ModelViewSet):
    queryset = RoomStats.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomStatsSerializer
    filter_backends = [
        filters.SearchFilter
    ]
    search_fields = ['house__id']

class DevicesView(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DevicesSerializer

class RoomControlView(viewsets.ModelViewSet):
    queryset = RoomControl.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomControlSerializer  

class LeagueView(viewsets.ModelViewSet):
    queryset = League.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeagueSerializer