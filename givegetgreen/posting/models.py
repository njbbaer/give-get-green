from django.db import models

# Create your models here.
class Posting(models.Model):
    name = models.TextField(default="")
    email = models.TextField(default="")
    address = models.TextField(default="")
    phone = models.TextField(default="")
    title = models.TextField(default="")
    category = models.TextField(default="")
    description= models.TextField(default="")