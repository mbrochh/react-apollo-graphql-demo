import graphene

import simple_app.schema


class Mutation(simple_app.schema.Mutation, graphene.ObjectType):
    pass


class Query(simple_app.schema.Query, graphene.ObjectType):
    pass

    
schema = graphene.Schema(query=Query, mutation=Mutation)
