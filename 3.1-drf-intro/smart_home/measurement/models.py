from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor,  related_name="temperatures", on_delete=models.CASCADE)
    temperature = models.IntegerField()
    date_time_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='phones_img', null=True)

