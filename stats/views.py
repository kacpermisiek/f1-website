from django.shortcuts import render
from django.http import HttpResponse


def stats_drivers(request):
    return render(request, 'stats/stats_drivers.html', {'title': 'F1 Blog Drivers Stats'})
