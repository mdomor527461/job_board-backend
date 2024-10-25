from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    image_url = models.URLField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.username

