import graphene
from models.schema import ModelQuery

class Query(ModelQuery, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)
