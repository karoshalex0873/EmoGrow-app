from django.db import models
from mimetypes import guess_type

# Create your models here.
class teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="assignments/")

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    status = models.CharField(
        max_length=50, default="Pending"
    )  # e.g., 'Pending', 'Answered'
    response = models.TextField(
        blank=True, null=True
    )  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
