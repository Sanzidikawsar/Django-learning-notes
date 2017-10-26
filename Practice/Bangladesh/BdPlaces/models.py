from django.db import models

# Create your models here.
class Place(models.Model):
    division = models.CharField(max_length=15)

    def __str__(self):
        return self.division

class SubPlace(models.Model):
    foreign = models.ForeignKey(Place)
    district = models.CharField(max_length=15)

    def __str__(self):
        return self.district
