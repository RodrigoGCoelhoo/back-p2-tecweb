from rest_framework import viewsets
from . import models
from . import serializers

class CityWeatherViewset(viewsets.ModelViewSet):
  queryset = models.CityWeather.objects.all()
  serializer_class = serializers.CityWeatherSerializer