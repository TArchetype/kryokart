from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField

# Create your models here.

class GPS(models.Model):
    longtitude = models.CharField(max_length=15)
    latitude = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.longtitude) + ", " + str(self.latitude)