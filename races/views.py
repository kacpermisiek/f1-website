from django.db.models import Sum
from django.shortcuts import render
from .models import Race, Driver, DriverPosition


def races(request):

    races = Race.objects.all().order_by('date')
    drivers = Driver.objects.all().order_by('-points')
    driverPosition = DriverPosition.objects.all().order_by('-race_points')


    context = {
        'races': races,
        'drivers': drivers,
        'driverPosition': driverPosition,
        'title': 'Wyniki wyścigów',
        'iterateover': range(1, 2),

    }
    return render(request, 'races/timetable.html', context)
