from weatherdb.viewsets import CityWeatherViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('city', CityWeatherViewset)

