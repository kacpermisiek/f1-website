from django.urls import path
from . import views


urlpatterns = [
    path('', views.races, name='races'),

]
