from django.db import models
from users.models import User
from django.db import models
from cloudinary.models import CloudinaryField
class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.name


class Job(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = CloudinaryField('resume', resource_type='raw',null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.applicant.username} applied for {self.job.title}'


