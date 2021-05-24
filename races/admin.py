from django.contrib import admin
from .models import Race, Team, Driver, DriverPosition

admin.site.register(Driver)
admin.site.register(Race)
admin.site.register(DriverPosition)
admin.site.register(Team)

