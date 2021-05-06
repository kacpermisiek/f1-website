from django.contrib import admin
from .models import Race, Driver, DriverPosition

admin.site.register(Driver)
admin.site.register(Race)
admin.site.register(DriverPosition)

