from django.db import models
from django.utils.translation import gettext as _


class Career(models.Model):
    code = models.CharField(max_length=2)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description

class Countries(models.Model):
    code = models.CharField(max_length=2)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description

class Cities(models.Model):
    code = models.CharField(max_length=2)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    career = models.ForeignKey(Career,
                             on_delete=models.CASCADE) 
    date_birth =models.DateField(_('Date of Birth'))
    phone_number = models.CharField(max_length=20)
    country = models.ForeignKey(Countries,
                             on_delete=models.CASCADE) 
    city = models.ForeignKey(Cities,
                             on_delete=models.CASCADE)  
    def __str__(self):
        return self.name
