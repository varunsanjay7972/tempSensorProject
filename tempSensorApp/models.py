from django.db import models



class TemperatureReading(models.Model):
    temperature = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
