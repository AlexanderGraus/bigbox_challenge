import graphene

import ingredients.schema
import ingredients.schema


class Query(
    ingredients.schema.Query,  # Add your Query objects here
    graphene.ObjectType
):
    pass

#TODO: tengo que comentar esto por ahora par que el tutorial siga funcionando

# class Mutation(
#     ingredients.schema.Mutation, # Add your Mutation objects here
#     graphene.ObjectType
# ):
#     pass

schema = graphene.Schema(query=Query,) #mutation=Mutation)