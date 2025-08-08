# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('C', 'Customer'),
        ('M', 'Mechanic'),
        ('A', 'Admin'),
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='C')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username