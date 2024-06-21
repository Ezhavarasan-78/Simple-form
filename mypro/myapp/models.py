from django.db import models

class Form(models.Model):
    username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=30)
