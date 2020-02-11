from django.db import models
from student.models import (Student)

class Dues_Option(models.Model):
    code = models.CharField(max_length=2)
    value = models.IntegerField()
    
    def __str__(self):
        return self.code


class Type_Payment(models.Model):
    code = models.CharField(max_length=2)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description


class Payment(models.Model):
    student = models.ForeignKey(Student, 
                                     on_delete=models.CASCADE)
    payment_type = models.ForeignKey(Type_Payment, 
                                     on_delete=models.CASCADE)
    dues = models.ForeignKey(Dues_Option,
                             on_delete=models.CASCADE,blank=True, null=True)
  
    def __str__(self):
        return self.student.name
