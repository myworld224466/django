#from typing_extensions import Self
from django.db import models
from datetime import datetime

# Create your models here.

class Department(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('Department Name',max_length=100)
    def __str__(self):
        return self.name


class Employee(models.Model):
    DESIGNATION_CHOICES=[
        ('IT Manager','IT Manager'),
        ('Supervisor','Supervisor'),
        ('Developer','Developer')
        ]
    id=models.AutoField(primary_key=True)
    name=models.CharField('Employee Name',max_length=100)
    email=models.CharField('Employee Email',max_length=100)
    address=models.CharField('Employee Address',max_length=300)
    phone=models.CharField('Employee Phone',max_length=20)
    doj=models.DateField('Date of Joining',default=datetime.now,blank=True)
    designation=models.CharField('Designation',max_length=50,choices=DESIGNATION_CHOICES,default='Developer')
    salary=models.DecimalField('Employee Salary',max_digits=8,decimal_places=2,blank=True,null=True)
    photo=models.FileField('Employee Photo',upload_to='employee',default='employee/blank.jpg',blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    #Cascade means if someone delete the Department all the sub trees will be deleted too.
    
    
    def __str__(self):
        return self.name
    