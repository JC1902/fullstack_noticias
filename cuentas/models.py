from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario( AbstractUser ):
    edad = models.PositiveBigIntegerField(null = True, blank = True)