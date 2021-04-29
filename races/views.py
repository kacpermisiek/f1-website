from django.shortcuts import render
from django.http import HttpResponse


def races(request):
    return HttpResponse('<h1>Wyniki wyscigow</h1>')
