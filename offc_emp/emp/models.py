from django.db import models

# Create your models here.

class Department(models.Model):
    DEPT_CHOICES={
    ('None','None'),
    ('IT','IT'),
    ('Sales','Sales'),
    ('Admin','Admin'),
    ('Marketing','Marketing'),
  }
    
    name = models.CharField(max_length=100, choices=DEPT_CHOICES, default='None')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    ROLE_CHOICES={
        ('IT Manager', 'IT Manager'),
        ('IT Assistant','IT Assistant'),
        ('Sales Executive', 'Sales Executive'),
        ('Marketing Manager', 'Marketing Manager'),
        ('Marketing Executive','Marketing Executive'),
    }
    name = models.CharField(max_length=100, choices=ROLE_CHOICES ,default='None')

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()


    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)