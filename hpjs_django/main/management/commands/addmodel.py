from django.core.management.base import BaseCommand, CommandError
from main.models import HPJS_Model, Trial, Parameter, ParameterValue

class Command(BaseCommand):
  def handle(self, *args, **options):
    self.stdout.write("adding model to database", ending='\n')

    model1 = HPJS_Model(name="Mnist")
    model1.save()