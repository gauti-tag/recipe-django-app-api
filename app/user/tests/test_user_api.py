"""
Test for the user API
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    """ create and return a new user """
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """ Test the public feature of the user API."""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED) # Compare the http status response

        user = get_user_model().objects.get(email= payload['email'])
        self.assertTrue(user.check_password(payload['password'])) # Confirm is the password is correct

        self.assertNoIn('password', res.data) # password is not in the data response

    def test_user_width_email_exists_error(self):
        """ test error returned if user email exists"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }

        create_user(**payload) # Function to create a user
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """ Test an error is returned if password less than 5 chars """
        payload = {
            'email': 'test@axample.com',
            'password': 'pw',
            'name': ' Test Name',
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exists = get_user_model().objects.filter(email= payload['email']).exists()
        self.assertFalse(user_exists)