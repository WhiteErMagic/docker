from .models import Sensor, Measurement
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class MeasurementDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('temperature', 'date_time_updated')


class SensorDetailsSerializer(serializers.ModelSerializer):
    temperatures = MeasurementDetailsSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description', 'temperatures')