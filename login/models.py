from django.db import models

# Create your models here.
class Farmer(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phone=models.CharField(max_length=11)
    dob=models.DateField()
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=20)
    province=models.CharField(max_length=20)

    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname
    
class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

