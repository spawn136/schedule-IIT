from rest_framework import serializers


class ScheduleSerializers(serializers.Serializer):
    day = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    discipline = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    times = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    teacher = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
