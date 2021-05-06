from django.db import models


class Driver(models.Model):

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    points = models.IntegerField()

    def __str__(self):
        return self.name + self.surname


class Race(models.Model):

    country = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    date = models.DateField

    def __str__(self):
        return f"{self.track} at {self.country}"


class DriverPosition(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    race_points = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['driver', 'race']]


"""
drivers = (
    ('HAM', 'Lewis Hamilton'),
    ('VER', 'Max Verstappen'),
    ('NOR', 'Lando Norris'),
    ('', 'Valtteri Bottas'),
    ('', 'Charles Leclerc'),
    ('', 'Sergio Perez'),
    ('', 'Daniel Ricciardo'),
    ('', 'Carlos Sainz'),
    ('', 'Esteban Ocon'),
    ('', '	Pierre Gasly'),
    ('', 'Lance Stroll'),
    ('', 'Fernando Alonso'),
    ('', 'Yuki Tsunoda'),
    ('', 'Kimi Raikkonen'),
    ('', 'Antonio Giovinazzi'),
    ('', 'George Russell'),
    ('', 'Sebastian Vettel'),
    ('', 'Mick Schumacher'),
    ('', 'Nicholas Latifi'),
    ('', ''),
    ('', ''),
    ('', ''),
"""