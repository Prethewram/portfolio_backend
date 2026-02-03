from django.db import models

# Create your models here.

class devicedetails(models.Model):
    name = models.TextField()
    ip = models.CharField(max_length=100,null=True,blank=True)
    location = models.TextField(default="not available")

