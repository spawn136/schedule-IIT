from django.test import TestCase
from .func import *


class TestAddSchedule(TestCase):
    def test(self):
        k = addSchedule("Вт", "СИАОД", "12:40", "Кузнецов Игорь Андреевич")
        k.pop('id')
        self.assertEqual(k, {'day': 'Вт', 'discipline': 'СИАОД', 'times': '12:40',
                             'teacher': 'Кузнецов Игорь Андреевич'})

    def test1(self):
        k = addSchedule("Пн", "Программирование на языке Python", "18:00", "Сергушев Артём Алексеевич")
        k.pop('id')
        self.assertEqual(k, {'day': 'Пн', 'discipline': 'Программирование на языке Python', 'times': '18:00',
                             'teacher': 'Сергушев Артём Алексеевич'})


class TestGetSchedule(TestCase):
    def test_get(self):
        k = getSchedule("Пн", "Информатика", "19:30", "Макаров Павел Андреевич")
        self.assertEqual(k[0], {
            "id": 7,
            "day": "Пн",
            "discipline": "Информатика",
            "times": "19:30",
            "teacher": "Макаров Павел Андреевич"
        })

    def test_get2(self):
        k = getSchedule("Cб", "Программирование на языке Python", "18:00", "Сергушев Артём Алексеевич")
        self.assertEqual(k[0], {
            "id": 13,
            "day": "Cб",
            "discipline": "Программирование на языке Python",
            "times": "18:00",
            "teacher": "Сергушев Артём Алексеевич"
        })
    def test_get3(self):
        k = getSchedule("Чт", "СИАОД", "12:40", "Кузнецов Игорь Андреевич")
        self.assertEqual(k[0], {
            "id": 12,
            "day": "Чт",
            "discipline": "СИАОД",
            "times": "12:40",
            "teacher": "Кузнецов Игорь Андреевич"
        })
