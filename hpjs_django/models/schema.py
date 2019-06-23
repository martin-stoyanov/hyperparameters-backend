import graphene
from graphene_django.types import DjangoObjectType
from .models import HPJS_Model

class ModelType(DjangoObjectType):
  class Meta:
    model = HPJS_Model

class ModelQuery(object):
  all_models = graphene.List(ModelType)

  def resolve_all_models(self, info, **kwargs):
    return HPJS_Model.objects.all()
