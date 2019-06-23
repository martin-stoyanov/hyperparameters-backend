import graphene
from graphene_django.types import DjangoObjectType
from .models import HPJS_Model, Trial

class ModelType(DjangoObjectType):
  class Meta:
    model = HPJS_Model

class TrialType(DjangoObjectType):
  class Meta:
    model = Trial

class ModelQuery(object):
  all_models = graphene.List(ModelType)
  all_trials = graphene.List(TrialType)

  def resolve_all_models(self, info, **kwargs):
    return HPJS_Model.objects.all()

  def resolve_all_trials(self, info, **kwargs):
    return TrialType.objects.select_related('hpjs_model').all()
