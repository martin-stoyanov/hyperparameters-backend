from django.core.management.base import BaseCommand, CommandError
from main.models import HPJS_Model, Trial, Parameter, ParameterValue

class Command(BaseCommand):
  def handle(self, *args, **options):
    # deleting previous records so we can re-run the admin-command
    HPJS_Model.objects.all().delete()
    Trial.objects.all().delete()
    Parameter.objects.all().delete()
    ParameterValue.objects.all().delete()

    self.stdout.write("adding model to database", ending='\n')

    model1 = HPJS_Model(name="Mnist")
    model1.save()
    trial1 = Trial(trial=1, start_time="2019-02-12 12:12", 
      end_time="2019-02-12 12:12", accuracy=0.3, hpjs_model=model1)
    trial1.save()