from .models import *
from django.db import connection


def addSchedule(day, discipline, times, teacher):
    schedule = Schedule(day=day, discipline=discipline, times=times, teacher=teacher)
    schedule.save()
    return schedule

def getSchedule(day, discipline, times, teacher):
    try:
        if  day == '' and discipline == '' and times == '' and teacher == '':
            schedule = Schedule.objects.all()
        else:
            schedule = Schedule.objects.filter(day=day) | Schedule.objects.filter(discipline=discipline) | Schedule.objects.filter(times=times) | Schedule.objects.filter(teacher=teacher)
    except Schedule.DoesNotExist:
        schedule = None

    print(day, discipline, times, teacher)

    return schedule

