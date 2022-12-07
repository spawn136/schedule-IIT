from django.db import models


# Create your models here.
class Schedule(models.Model):
    def __init__(self, day, discipline, times, teacher):
        self.day = day
        self.discipline = discipline
        self.times = times
        self.teacher = teacher
