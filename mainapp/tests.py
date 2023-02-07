from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from mainapp.models import Event, EventType
from mainapp.serializers import EventSerializer


class EventTests(APITestCase):
    def setUp(self):
        user_test = User.objects.create_user(username='test', password='12345')
        user_test.save()
        self.user_test_token = Token.objects.create(user=user_test)

        self.event_type_attributes = {
            'name': 'Test'
        }
        self.event_type = EventType.objects.create(**self.event_type_attributes)

        self.event_attributes = {
            'user': user_test,
            'event_type': self.event_type,
            'info': {
                'info1': 'ok1',
                'info2': 'ok2'
            },
            'timestamp': "2018-03-29T13:34:00.000",
        }

        self.event = Event.objects.create(**self.event_attributes)
        self.serializer = EventSerializer(instance=self.event)

    def test_contains_expected_fields(self):
        """ If the serializer has the exact attributes it is expected to. """
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['event_type', 'info', 'timestamp'])

    def test_event_type_field_content(self):
        """ If the serializer produces the expected data to 'event_type' field. """
        data = self.serializer.data
        self.assertEqual(data['event_type'], self.event_attributes['event_type'].name)

    def test_info_field_content(self):
        """ If the serializer produces the expected data to 'info' field. """
        data = self.serializer.data
        self.assertEqual(data['info'], self.event_attributes['info'])

    def test_create_invalid_event(self):
        """ If user isn't authorized --> HTTP_401_UNAUTHORIZED. """
        response = self.client.post(reverse('create_event'), self.serializer.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_valid_event(self):
        """ If user is authorized --> HTTP_201_CREATED. """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test_token.key)
        response = self.client.post(reverse('create_event'), self.serializer.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
