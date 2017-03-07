from django.db import models

# Create your models here.
class Posting(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    item_category = models.CharField(max_length=100)
    item_description= models.CharField(max_length=100)