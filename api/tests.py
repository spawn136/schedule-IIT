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
             }
        ])
