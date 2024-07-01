# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailsSerializer


class SensorViewCreate(ListCreateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class SensorViewUpdate(RetrieveUpdateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class SensorViewGet(RetrieveUpdateAPIView):
    serializer_class = SensorDetailsSerializer
    queryset = Sensor.objects.all()


class MeasurementViewCreate(CreateAPIView, ListCreateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
