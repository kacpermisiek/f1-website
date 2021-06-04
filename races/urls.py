from django.urls import path
from . import views


urlpatterns = [
    path('harmonogram', views.races, name='races'),
    path('tabela_kierowcy', views.tabela_kierowcy, name='tabela_kierowcy'),

]
