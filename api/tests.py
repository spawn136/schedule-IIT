from django.urls import reverse
from rest_framework.test import APITestCase
import json


class DBTests(APITestCase):
    def test_correct(self):
        url = reverse('get', args=['Пн', 'Линейная Алгебра', '16:20', 'Макаров Павел Андреевич'])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content),
        [
            {"id": 1,
             "day": 'Пн',
             "discipline": 'Линейная Алгебра',
             "times": '16:20',
             "teacher": 'Макаров Павел Андреевич'
             },
        ])
    def test_correct2(self):
        url = reverse('get', args=['Вт', 'Математический Анализ', '16:20', 'Салов Владислав Дмитриевич'])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content),
        [
            {"id": 2,
             "day": 'Вт',
             "discipline": 'Математический Анализ',
             "times": '16:20',
             "teacher": 'Салов Владислав Дмитриевич'
             },
        ])
    def test_correct3(self):
        url = reverse('get', args=['Ср', 'Программирование на языке JAVA', '14:20', 'Кутергин Андрей Вениаминович'])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content),
        [
            {"id": 3,
             "day": 'Ср',
             "discipline": 'Программирование на языке JAVA',
             "times": '14:20',
             "teacher": 'Кутергин Андрей Вениаминович'
             },
        ])
    def test_correct4(self):
        url = reverse('get', args=['Чт', 'Информатика', '18:00', 'Тульцова Анастасия Денисова'])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content),
        [
            {"id": 4,
             "day": 'Чт',
             "discipline": 'Информатика',
             "times": '18:00',
             "teacher": 'Тульцова Анастасия Денисова'
             },
        ])
    def test_correct5(self):
        url = reverse('get', args=['Пт', 'Математический Анализ', '18:00', 'Бугров Андрей Павлович'])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content),
        [
            {"id": 5,
             "day": 'Пт',
             "discipline": 'Математический Анализ',
             "times": '18:00',
             "teacher": 'Бугров Андрей Павлович'
             },
        ])
    def test_correct6(self):
        url = reverse('get', args=['Сб', 'Процедурное программирование', '19:40', 'Сердюков Александр Андреевич'])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content),
        [
            {"id": 6,
             "day": 'Сб',
             "discipline": 'Процедурное программирование',
             "times": '19:40',
             "teacher": 'Сердюков Александр Андреевич'
             },
        ])


