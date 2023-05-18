from django.db import models

# Create your models here.

class Scholl(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)


class Student(models.Model):
    scholl=models.ForeignKey(Scholl,on_delete=models.CASCADE,related_name='students')
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()