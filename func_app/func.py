from .models import *
from django.db import connection
import sqlite3


def addSchedule(day, discipline, times, teacher):
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('INSERT INTO func_app_schedule ("day", "discipline", "times", "teacher") VALUES (?,?,?,?) RETURNING *',
                (day, discipline, times, teacher))
    row = cur.fetchone()

    cur.close()
    con.commit()

    return dict(row)


def getSchedule(day, discipline, times, teacher):
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(
        '''SELECT * FROM func_app_schedule WHERE "day" LIKE ? AND "discipline" LIKE ? AND "times" LIKE ? AND "teacher" LIKE ? ''',
        (f"%{day}%", f"%{discipline}%", f"%{times}%", f"%{teacher}%"))
    row = cur.fetchall()
    cur.close()
    con.commit()
    row = [dict(i) for i in row]
    print(row)
    return row
#    try:
#       if day == '' and discipline == '' and times == '' and teacher == '':
#           schedule = Schedule.objects.all()
#       else:
#           schedule = Schedule.objects.filter(day=day) | Schedule.objects.filter(
#               discipline=discipline) | Schedule.objects.filter(times=times) | Schedule.objects.filter(teacher=teacher)
#   except Schedule.DoesNotExist:
#       schedule = None

#   print(day, discipline, times, teacher)

#   return schedule
