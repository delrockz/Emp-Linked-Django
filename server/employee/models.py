from django.db import models

# Create your models here.
class Employee(models.Model):
    fname=models.CharField(max_length=50,null=False)
    lname = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=False,unique=True)
    contact = models.IntegerField(null=True)
    username = models.CharField(max_length=20,null=False,unique=True)
    pwd = models.CharField(max_length=20,null=False)
    dob = models.DateField(null=True)
    bio = models.CharField(max_length=350)
    jobrole = models.CharField(max_length=50)



