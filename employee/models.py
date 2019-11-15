from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)  
    class Meta:  
        db_table = "department" 
 
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)  
    emp_email = models.EmailField()  
    emp_salary = models.IntegerField(default=0)
    dept_name = models.ForeignKey(Department,on_delete = models.CASCADE,null=True)
    
    class Meta:  
        db_table = "employee"
