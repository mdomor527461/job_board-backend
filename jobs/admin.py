from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Job)
admin.site.register(models.JobApplication)
admin.site.register(models.Category)
