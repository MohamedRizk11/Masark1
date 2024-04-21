from django.contrib import admin
from .models import Station , Ticket,Users,FamousPlace

# Register your models here.
class famousplaces(admin.TabularInline):
    model = FamousPlace

class stationplace(admin.ModelAdmin):
    inlines=[famousplaces] 

class famousplace(admin.ModelAdmin):
    list_display=['name','station_id','station']       

admin.site.register(Station,stationplace)
admin.site.register(Ticket)
admin.site.register(Users)
admin.site.register(FamousPlace,famousplace)