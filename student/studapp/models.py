from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField(max_length=20)
    dob=models.DateField()
    phy=models.FloatField()
    chem=models.FloatField()
    maths=models.FloatField()
    cs=models.FloatField()
    per=models.FloatField()