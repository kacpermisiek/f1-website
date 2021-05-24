from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return self.name


class Driver(models.Model):

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return self.name + self.surname


class Race(models.Model):

    country = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.track} at {self.country}"


class DriverPosition(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    race_points = models.PositiveSmallIntegerField()
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"track: {self.race.track}   driver: {self.driver.surname}  points: {self.race_points}"

    class Meta:
        unique_together = [['driver', 'race']]

