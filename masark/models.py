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


class Station(models.Model):
    station_id = models.IntegerField(_("Station_Id"))  # Renamed to lowercase 'id'
    name = models.CharField(_("Name"), max_length=20)
    famousPlaces = models.CharField(_("FamousPlaces"), max_length=50)
    
    def __str__(self):
        return self.name
   

class Ticket(models.Model):
    stationid = models.ForeignKey("Station", verbose_name=_("StationID"), related_name="ticket_station", on_delete=models.SET_NULL, null=True)
    cost = models.FloatField(_("Cost"))
    time = models.FloatField(_("Time"))

    def __str__(self):
        return str(self.stationid)  # Ensure to return a string representation