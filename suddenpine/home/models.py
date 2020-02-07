from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here. 

class HouseDetails(models.Model):
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    houseNumber = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    resident = models.ForeignKey(User, related_name="home", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.houseNumber, self.address, self.city, self.postcode

# Stats for/per House (current)

class HouseStats(models.Model):
    solarproduction = models.DecimalField(max_digits=7, decimal_places=2)
    batterycharge = models.DecimalField(max_digits=7, decimal_places=2)
    energyconsumtion = models.DecimalField(max_digits=7, decimal_places=2)
    moneysaved = models.DecimalField(max_digits=7, decimal_places=2)
    house = models.OneToOneField('HouseDetails', on_delete=models.CASCADE)

# Stats logged as the week progesses
# Daily Energy Consumption (weekly, home)
# Daily Solar Production (weely, home)

class WeeklyLogs(models.Model):
    solarweekly = models.DecimalField(max_digits=7, decimal_places=2)
    energyweelky = models.DecimalField(max_digits=7, decimal_places=2)
    house = models.ForeignKey('HouseDetails', on_delete=models.CASCADE)

# Energy Consumption by Room (weekly)
# May include : roomtemp = models.DecimalField(max_digits=7, decimal_places=2)

class RoomStats(models.Model):
    roomtype = models.CharField(max_length=50)
    energy = models.DecimalField(max_digits=7, decimal_places=2)
    house = models.ForeignKey('HouseDetails', on_delete=models.CASCADE)

# Energy Consumption by Devices (devices name, locattion(room), conpsumption)

class Devices(models.Model):
    device = models.CharField(max_length=50)
    deviceconsumption = models.DecimalField(max_digits=7, decimal_places=2)
    room = models.OneToOneField('RoomStats', on_delete=models.CASCADE)

# Lighting and heating controls per room

class RoomControl(models.Model):
    roomID = models.OneToOneField('RoomStats', on_delete=models.CASCADE)
    heating = models.SmallIntegerField()
    light = models.SmallIntegerField()
    window = models.BooleanField(default=False)
    door = models.BooleanField(default=False)
    safetyalarm = models.BooleanField(default=False)

# Energy score league

class League(models.Model):
    score = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    house = models.ForeignKey('HouseDetails', on_delete=models.CASCADE)