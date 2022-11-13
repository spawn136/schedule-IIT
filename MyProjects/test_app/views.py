from django.shortcuts import render
from django.http import HttpResponse
from func_app.func import *


# Create your views here.
def queryGetShedule(request):
    day = request.GET.get("day")
    discipline = request.GET.get("discipline")
    times = request.GET.get("times")
    teacher = request.GET.get("teacher")

    schedule = getSchedule(day, discipline, times, teacher)

    print(id)
    return HttpResponse((f"ID: {obj.id} | День недели: {obj.day}, Дисциплина: {obj.discipline}, Время проведения: {obj.times}, Преподаватель: {obj.teacher}<br>"
                        for obj in schedule) if len(schedule) else f"Нет в базе")
