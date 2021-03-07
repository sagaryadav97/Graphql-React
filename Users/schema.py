import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Users, Skills


class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        fields = ('id','name','email','skillt')

class SkillsType(DjangoObjectType):
    class Meta:
        model = Skills  
        fields = ('id','skills')

class UsersTypeNode(DjangoObjectType):
    class Meta:
        model = Users
        filter_fields = {
            'id',
        }
        interfaces = (graphene.relay.Node, )

class SkillsTypeNOde(DjangoObjectType):
    class Meta:
        model = Skills  
        filter_fields = {
            'id',
        }
        interfaces = (graphene.relay.Node, )
        

class Query(graphene.ObjectType):
  Users = graphene.List(UsersType)
  Skills = graphene.List(SkillsType)

  viewer = graphene.relay.Node.Field(UsersTypeNode)
  org = graphene.relay.Node.Field(SkillsTypeNOde)
  all_users = DjangoFilterConnectionField(UsersTypeNode)
  all_orgs = DjangoFilterConnectionField(SkillsTypeNOde)
    # def resolve_Users(root,info):
    #     return Users.objects.all()
  def resolve_Users(root,info):
        return Users.objects.all()
    
  def resolve_Skills(root,info):
        return Skills.objects.all()
        
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