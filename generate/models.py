from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Brand(models.Model):
    name = models.CharField(max_length=100)

class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Form1(models.Model):
     input_digi_port=models.IntegerField(default=0,validators=[ MinValueValidator(1),MaxValueValidator (20)])
class Form2(models.Model):
     input_digi_port=models.IntegerField(default=0,validators=[ MinValueValidator(1),MaxValueValidator (20)])
class Form3(models.Model):
     input_digi_port=models.IntegerField(default=0,validators=[ MinValueValidator(1),MaxValueValidator (20)])
class Form4(models.Model):
    input_digi_port=models.IntegerField(default=0,validators=[ MinValueValidator(1),MaxValueValidator (20)])
class promt(models.Model):
     promt=models.CharField(max_length=800)    
