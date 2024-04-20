from django.contrib import admin
from .models import Station , Ticket,Users


# Register your models here.
admin.site.register(Station)
admin.site.register(Ticket)
admin.site.register(Users)