from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    # path('stats_drivers/', views.stats_drivers, name='blog-stats_drivers'),
    # path('stats_teams/', views.about, name='blog-stats_teams')
]