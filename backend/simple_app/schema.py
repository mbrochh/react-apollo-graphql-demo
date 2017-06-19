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
        if not context.user.is_authenticated():
            return CreateMessage(form_errors=json.dumps('Please login!'))
        message = models.Message.objects.create(
            user=context.user, message=args.get('message'))
        return CreateMessage(message=message, form_errors=None)


class Mutation(graphene.AbstractType):
    create_message = CreateMessage.Field()


class Query(graphene.AbstractType):
    all_messages = DjangoFilterConnectionField(MessageType)

    def resolve_all_messages(self, args, context, info):
        return models.Message.objects.all()
