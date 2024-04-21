from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

Status_type=(
    ("Normal","Normal"),
    ("Disabled","Disabled"),

)

class Users(models.Model):
    user_id=models.IntegerField(_("User_ID"))
    status=models.CharField(_("Status"),max_length=10,choices=Status_type)

    def __str__(self):
        return str(self.user_id)

class FamousPlace(models.Model):
    station = models.ForeignKey("Station", related_name='station_place', on_delete=models.SET_NULL,null=True)

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Station(models.Model):
    station_id = models.IntegerField(_("Station_Id"),unique=True)  # Renamed to lowercase 'id'
    name = models.CharField(_("Name"), max_length=20)
    

    
    def __str__(self):
        return self.name
    


class Ticket(models.Model):
    from_station = models.ForeignKey(Station, related_name='from_station', on_delete=models.SET_NULL,null=True)
    to_station = models.ForeignKey(Station, related_name='to_station', on_delete=models.SET_NULL,null=True)
    cost = models.FloatField(_("Cost"))
    time = models.FloatField(_("Time"))

    def __str__(self):
        return f"Ticket from {self.from_station} to {self.to_station}"  # Ensure to return a string representation