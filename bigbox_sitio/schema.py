import graphene

import ingredients.schema
import ingredients.schema

class Query(
    ingredients.schema.Query, # Add your Query objects here
    graphene.ObjectType
):
    pass

class Mutation(
    ingredients.schema.Mutation, # Add your Mutation objects here
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)