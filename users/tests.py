from django.test import TestCase

# Create your tests here.
from django.test import Client

from users.models import User

good_user_create_dto = {
    "username": "test",
    "email": "test@example.com",
    "password": "PCcLFEMb2ubgkT",
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

    def test_user_signin(self):
        self.client.post(
            "/users/",
            good_user_create_dto,
        )
        response = self.client.post(
            "/api-token-auth/",
            {
                "username": good_user_create_dto["username"],
                "password": good_user_create_dto["password"],
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_user_signin_bad_password(self):
        self.client.post(
            "/users/",
            good_user_create_dto,
        )
        response = self.client.post(
            "/api-token-auth/",
            {
                "username": good_user_create_dto["username"],
                "password": "BAD PASSWORD",
            },
        )
        self.assertEqual(response.status_code, 400)
