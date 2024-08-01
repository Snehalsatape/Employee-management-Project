from django.db import models

class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.fname} {self.lname}'
