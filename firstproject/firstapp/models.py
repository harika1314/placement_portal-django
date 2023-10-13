from django.db import models
from tabnanny import verbose
 

# Create your models here.
class List(models.Model):
    sno=models.CharField(max_length=10)
    companies=models.CharField(max_length=20)
      
      
      
    def __str__(self):
        return self.sno