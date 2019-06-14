from django.db import models

# Create your models here.
class HPJS_Model(models.Model):
  name = models.CharField(max_length=50)

class Trial(models.Model):
  trial = models.IntegerField()
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  accuracy = models.FloatField()
  hpjs_model = models.ForeignKey(HPJS_Model, on_delete=models.CASCADE)

class Parameter(models.Model):
  parameter_name = models.CharField(max_length=50)
  hpjs_model = models.ForeignKey(HPJS_Model, on_delete=models.CASCADE)

class ParameterValue(models.Model):
  value = models.CharField(max_length=50)
  trial = models.ForeignKey(Trial, on_delete=models.CASCADE)
  parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)