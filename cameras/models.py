from django.db import models


class Camera(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
