from rest_framework import serializers
from .models import HouseDetails, HouseStats, WeeklyLogs, RoomStats, Devices, RoomControl, League

# Serializers

class HouseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseDetails
        fields = '__all__'

class HouseStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseStats
        fields = ('__all__')

class WeeklyLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyLogs
        fields = '__all__'

class RoomStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomStats
        fields = '__all__'

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'

class RoomControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomControl
        fields = '__all__'

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'                      