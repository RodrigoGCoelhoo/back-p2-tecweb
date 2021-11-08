from django.db import models

# Create your models here.
class CityWeather(models.Model):
  cidade = models.CharField(max_length=100)
  lat = models.CharField(max_length=10)
  long = models.CharField(max_length=10)