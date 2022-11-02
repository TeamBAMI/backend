from django.test import TestCase

# Create your tests here.
from django.test import Client

from users.models import User

good_user_create_dto = {
    "username": "test",
    "email": "test@example.com",
    "password": "testpassword",
    "type": "STUDENT",
}


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_list(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 403)

    def test_user_create(self):
        response = self.client.post(
            "/users/",
            good_user_create_dto,
        )
        self.assertEqual(response.status_code, 201)

    def test_user_create_bad_type(self):
        response = self.client.post(
            "/users/",
            {
                **good_user_create_dto,
                "type": "I AM NOT A VALID TYPE",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_approved_business_user_create(self):
        response = self.client.post(
            "/users/",
            {
                **good_user_create_dto,
                "type": "APPROVED_BUSINESS",
            },
        )
        self.assertEqual(response.status_code, 400)
