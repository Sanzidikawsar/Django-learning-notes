from django.db import models

# Create your models here.
class Places(models.Model):
    division = models.CharField(max_length=15)