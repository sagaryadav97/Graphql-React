import graphene
from graphene_django import DjangoObjectType
from .models import Users


class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        fields = ('id','name','email','skills_set')

class Query(graphene.ObjectType):
    all_users = graphene.Field(UsersType,id=graphene.Int())
    Users = graphene.List(UsersType)
    
    def resolve_Users(root,info):
        return Users.objects.all()
    
    def resolve_all_users(root,info,id):
        return Users.objects.get(pk=id)
    
        
class CreateUsers(graphene.Mutation):
    class Arguments:
        name  = graphene.String(required=True)
        email  = graphene.String()
        skills_set  = graphene.String(required=True)
        
    users = graphene.Field(UsersType)
    
    @classmethod
    def mutate(cls,root,info,name,email,skills_set):
        users = Users(name=name,email=email,skills_set=skills_set)
        users.save()
        return CreateUsers(users=users)

class UpdateUsers(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name  = graphene.String(required=True)
        email  = graphene.String()
        skills_set  = graphene.String(required=True)
        
    users = graphene.Field(UsersType)
    
    @classmethod
    def mutate(cls,root,info,id,name,email,skills_set):
        users = Users.objects.get(id=id)
        users.name = name
        users.email = email
        users.skills_set = skills_set
        users.save()
        return UpdateUsers(users=users)

class Mutation(graphene.ObjectType):
    CreateUsers = CreateUsers.Field()
    UpdateUsers = UpdateUsers.Field()
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)