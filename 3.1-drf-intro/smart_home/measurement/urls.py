from django.urls import path
from .views import SensorViewCreate, MeasurementViewCreate, SensorViewUpdate, SensorViewGet

urlpatterns = [
    path('sensors/', SensorViewCreate.as_view()),
    path('add/', MeasurementViewCreate.as_view()),
    path('sensors/<int:pk>', SensorViewUpdate.as_view()),
    path('sensor/<int:pk>', SensorViewGet.as_view()),
]
