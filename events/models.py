from django.db import models
import datetime
# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=500)
    event_month = models.CharField(max_length=8)
    event_day = models.SmallIntegerField()
    event_description = models.TextField()
    event_type = models.CharField(max_length=300)
    event_link = models.CharField(max_length=500)
    event_food = models.BooleanField

    def __str__(self):
        return self.event_name

class BuildInfo(models.Model):
    build_month = models.IntegerField()
    build_year = models.IntegerField()
    build_month_string = models.CharField(max_length=8)

    def __str__(self):
        return self.build_month_string
