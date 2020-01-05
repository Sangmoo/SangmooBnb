from django.contrib.auth.models import AbstractUser
from django.db import models

# Import Model
class User(AbstractUser):

    """ Custom User Model """  # Class Info.

    GENDER_MALE = "male"  # Constant
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    # Tuple
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="", blank=True)
