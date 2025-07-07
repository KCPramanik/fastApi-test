from tortoise import fields
from tortoise.models import Model


class Role(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(min_length =2,max_length = 50)

    class Meta:
        table = "role"

        
class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    age = fields.IntField()
    vill = fields.CharField(max_length=100)
    state = fields.CharField(max_length=100)
    pin = fields.IntField()
    role: fields.ForeignKeyRelation[Role] = fields.ForeignKeyField(
        "models.Role", related_name="users", null=True
    )
    
    class Meta:
        table = "users"

    # def __str__(self):
    #     return self.name

