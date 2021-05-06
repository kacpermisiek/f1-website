from django.shortcuts import render

basic_table = [
    {
        'country': 'Bahrajn',
        'track': 'Sakhir',
        'date': '21.03.2021r.'
    },

    {
        'country': 'Włochy',
        'track': 'Imola',
        'date': '21.03.2021r.'
    },
]


def races(request):
    context = {
        'races': basic_table,
        'title': 'Wyniki wyścigów',

    }
    return render(request, 'races/timetable.html', context)
