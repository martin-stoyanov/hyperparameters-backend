from django.db import models

# Create your models here.
class mainModel(models.Model):
  txt = models.CharField(max_length=10)