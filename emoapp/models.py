from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

