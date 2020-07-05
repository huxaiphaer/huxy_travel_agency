from django.db import models


class Destinations(models.Model):
    location = models.CharField(max_length=20)
    tour_type = models.CharField(max_length=20)
    danger_type = models.CharField(max_length=20)

    def __str__(self):
        return self.location


class TourPackages(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=1)
    destinations = models.ManyToManyField(Destinations)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s: %s' % (self.name, self.capacity)
