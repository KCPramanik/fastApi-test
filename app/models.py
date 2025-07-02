from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    age = fields.IntField()
    vill = fields.CharField(max_length=100)
    state = fields.CharField(max_length=100)
    pin = fields.IntField()
    
    class Meta:
        table = "users"

    # def __str__(self):
    #     return self.name
