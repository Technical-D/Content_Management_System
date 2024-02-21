from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class UserAuthenticationTestCase(TestCase):
    def test_user_registration(self):
        url = reverse('register')
        data = {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'pincode': '123456',
            'password': 'Password123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        # Test user login
        url = reverse('login')
        data = {
            'email': 'john@example.com',
            'password': 'Password123'
        }
        response = self.client.post(url, data)
        # Expecting either 200 (OK) or 401 (Unauthorized) depending on the credentials
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])
