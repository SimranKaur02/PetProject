from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name;

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True,  blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)

