import graphene

from graphene import relay, ObjectType
from graphene_django import DjangoObjectType, DjangoListField
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoFormMutation
from graphene_django.forms.mutation import DjangoModelFormMutation

from graphql_relay import from_global_id


from django import forms
from django.db import models

from ingredients.models import Category, Ingredient


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )

class MyIngredient(graphene.ObjectType):
    name = graphene.String()

class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )
    
    extra_ingredient = graphene.String()
    
    def resolve_extra_ingredient(self, info):
        return "chimichurri!"

    def get_queryset(cls, queryset, info):
      # Filter out ingredients that have no name
      return queryset.exclude(name__exact="")

class IngredientConnection(relay.Connection):
    class Meta:
        node = IngredientNode

class IngredientMutation(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        id = graphene.ID()
    
    ingredient = graphene.Field(IngredientNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, id):
        ingredient = Ingredient.objects.get(pk=from_global_id(id)[1])
        ingredient.text = name
        ingredient.save()
        return IngredientMutation(question=ingredient)

class MyForm(forms.Form):
    name = forms.CharField()

class MyMutation(DjangoFormMutation):
    class Meta:
        form_class = MyForm

class Pet(models.Model):
    name = models.CharField()

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name',)

# This will get returned when the mutation completes successfully
class PetType(DjangoObjectType):
    class Meta:
        model = Pet

class PetMutation(DjangoModelFormMutation):
    pet = relay.Node.Field(PetType)

    class Meta:
        form_class = PetForm
        input_field_name = 'data'
        return_field_name = 'my_pet'

# django rest

from graphene_django.rest_framework.mutation import SerializerMutation
from snippets.serializers import SnippetSerializer

class MyAwesomeMutation(SerializerMutation):
    class Meta:
        serializer_class = SnippetSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        if 'id' in input:
            instance = Ingredient.objects.filter(
                id=input['id'], owner=info.context.user
            ).first()
            if instance:
                return {'instance': instance, 'data': input, 'partial': True}

            else:
                from django import http 
                raise http.Http404

        return {'data': input, 'partial': True}

class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = relay.ConnectionField(IngredientConnection)
    ingredientsList = DjangoListField(IngredientNode)
    
    def resolve_ingredients(root, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_ingredientsList(parent, info):
        # Only get ingredients that have categories
        return Ingredient.objects.select_related("category").all()
    
    # campo personalizado
    ingrediente = graphene.Field(MyIngredient, ingrediente_id=graphene.String())
    
    def resolve_ingrediente(root, info, ingrediente_id):
        ingrediente = Ingredient.objects.get(pk=ingrediente_id)
        return MyIngredient(name=ingrediente.name)


#devuelve la categoria solo si el usuario esta logueado
def resolve_category(root, info):
    if info.context.user.is_authenticated():
        return Category.objects.all()
    else:
        return Category.objects.none()
