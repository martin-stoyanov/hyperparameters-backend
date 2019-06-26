import graphene
from graphene_django.types import DjangoObjectType
from .models import HPJS_Model, Trial, Parameter, ParameterValue

class ModelType(DjangoObjectType):
  class Meta:
    model = HPJS_Model

class TrialType(DjangoObjectType):
  class Meta:
    model = Trial

class ParameterType(DjangoObjectType):
  class Meta:
    model = Parameter

class ParameterValueType(DjangoObjectType):
  class Meta:
    model = ParameterValue

class TrialInputType(graphene.InputObjectType):
  trial = graphene.Int()
  start_time = graphene.DateTime()
  end_time = graphene.DateTime()
  accuracy = graphene.Float()

class ModelAddMutation(graphene.Mutation):
  class Arguments:
    # The input arguments for this mutation
    name = graphene.String(required=True)
    trials = graphene.List(TrialInputType)
    
  # The class attributes define the response of the mutation
  hpjs_model = graphene.Field(ModelType)

  def mutate(self, info, name, trials):
    model = HPJS_Model(name=name)
    model.save()

    for trial in trials:
      t = Trial(trial=trial.trial, start_time=trial.start_time, end_time=trial.end_time, 
        accuracy=trial.accuracy, hpjs_model=model)
      t.save()

    # Notice we return an instance of this mutation
    return ModelAddMutation(hpjs_model=model)
    #return ModelAddMutation(hpjs_model=model, trial=trial1, parameter=parameter1,
    #  parametervalue=parametervalue1)

class ModelDeleteMutation(graphene.Mutation):
  class Arguments:
    # The input arguments for this mutation
    id = graphene.Int(required=True)

  # The class attributes define the response of the mutation
  id = graphene.Int()

  def mutate(self, info, id):
    model = HPJS_Model.objects.get(id=id)
    model.delete()
    # Notice we return an instance of this mutation
    return ModelDeleteMutation(id=id)


class ModelMutation:
    add_model = ModelAddMutation.Field()
    delete_model = ModelDeleteMutation.Field()

class ModelQuery(object):
  model = graphene.Field(ModelType,
    id=graphene.Int(),
    name=graphene.String())

  all_models = graphene.List(ModelType)
  all_trials = graphene.List(TrialType)
  all_parameters = graphene.List(ParameterType)
  all_parameter_values = graphene.List(ParameterValueType)

  def resolve_model(self, info, **kwargs):
    id = kwargs.get('id')
    name = kwargs.get('name')

    if id is not None:
            return HPJS_Model.objects.get(pk=id)

    if name is not None:
        return HPJS_Model.objects.get(name=name)

    return None

  def resolve_all_models(self, info, **kwargs):
    return HPJS_Model.objects.all()

  def resolve_all_trials(self, info, **kwargs):
    return Trial.objects.select_related('hpjs_model').all()

  def resolve_all_parameters(self, info, **kwargs):
    return Parameter.objects.select_related('hpjs_model').all()

  def resolve_all_parametervalues(self, info, **kwargs):
    return ParameterValue.objects.select_related('hpjs_model').all()
