import json
import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from . import models


class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        filter_fields = {'message': ['icontains']}
        interfaces = (graphene.Node, )


class CreateMessage(graphene.Mutation):
    class Input:
        message = graphene.String()

    form_errors = graphene.String()
    message = graphene.Field(lambda: MessageType)

    @staticmethod
    def mutate(root, args, context, info):
        if not args.get('message').strip():
            return CreateMessage(
                form_errors=json.dumps('Please enter a message!'))
        message = models.Message.objects.create(
            user=context.user, message=args.get('message'))
        return CreateMessage(message=message, form_errors=None)


class Mutation(graphene.AbstractType):
    create_message = CreateMessage.Field()


class Query(graphene.AbstractType):
    all_messages = DjangoFilterConnectionField(MessageType)

    message = graphene.Field(MessageType, id=graphene.ID())

    def resolve_all_messages(self, args, context, info):
        return models.Message.objects.all()

    def resolve_message(self, args, context, info):
        from graphql_relay.node.node import from_global_id
        pk = from_global_id(args.get('id'))[1]
        return models.Message.objects.get(pk=pk)
