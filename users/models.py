from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Types(models.TextChoices):
        APPROVED_BUSINESS = "APPROVED_BUSINESS", "Approved Business"
        BUSINESS = "BUSINESS", "Business"
        STUDENT = "STUDENT", "Student"

    type = models.CharField(max_length=20, choices=Types.choices, default=Types.STUDENT)
