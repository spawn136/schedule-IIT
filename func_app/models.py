from django.db import models


# Create your models here.
class Schedule (models.Model):
    day = models.TextField()
    discipline = models.TextField()
    times = models.TextField()
    teacher = models.TextField()

