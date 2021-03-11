from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Kacper',
        'title': 'Blog Post 1',
        'content': 'Pierwszy post testowy',
        'date_posted': '21 marca 2021'
    },

    {
        'author': 'Kacper2',
        'title': 'Blog Post 2',
        'content': 'Drugi post testowy',
        'date_posted': '22 marca 2021'
    },

    {
        'author': 'Kacper3',
        'title': 'Blog Post 3',
        'content': 'Trzeci post testowy',
        'date_posted': '21 marca 2021'
    },

    {
        'author': 'Kacper4',
        'title': 'Blog Post 4',
        'content': 'Czwarty',
        'date_posted': '21 marca 2021'
    },

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
