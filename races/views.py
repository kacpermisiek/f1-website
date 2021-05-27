from django.shortcuts import render
from .models import Race, Driver, DriverPosition, Team


def races(request):

    races = Race.objects.all().order_by('-date')
    drivers = Driver.objects.all().order_by('-points')
    driverPosition = DriverPosition.objects.all().order_by('position')
    team = Team.objects.all()

    context = {
        'races': races,
        'drivers': drivers,
        'driverPosition': driverPosition,
        'title': 'Wyniki wyścigów',

    }
    return render(request, 'races/timetable.html', context)


def general_drivers(request):
    drivers = Driver.objects.all().order_by('-points')