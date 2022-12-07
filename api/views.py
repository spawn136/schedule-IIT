from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Schedule
from .serializers import ScheduleSerializers
from func_app.func import getSchedule, addSchedule
from drf_spectacular.utils import extend_schema


class GetScheduleView(APIView):
    @extend_schema(request=ScheduleSerializers, responses=ScheduleSerializers)
    def get(self, request, day, discipline, times, teacher):
        s = getSchedule(day, discipline, times, teacher)
        print(s)
        schedule = (ScheduleSerializers(instance=st).data for st in s) if s is not None else []

        return Response(s)

class SetScheduleView(APIView):
    @extend_schema(request=ScheduleSerializers, responses=ScheduleSerializers)
    def set(self, request, day, discipline, times, teacher):
        s = addSchedule(day, discipline, times, teacher)
        # k.day = ScheduleSerializers(instance=k.day).data
        # k.discipline = ScheduleSerializers(instance=k.schedule.discipline).data
        # k.times = ScheduleSerializers(instance=k.times).data
        # k.teacher = ScheduleSerializers(instance=k.teacher).data
        return Response(s)
