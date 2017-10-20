from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=30)
    s_id = models.CharField(max_length=10)
    section = models.CharField(max_length=1)
    varsity = models.CharField(max_length=50)

    def __str__(self):
        return self.name
