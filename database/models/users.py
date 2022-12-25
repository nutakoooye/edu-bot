from tortoise.models import Model
from tortoise import fields


class Admins(Model):
    id = fields.IntField(pk=True)
    full_name = fields.TextField()
    tg_id = fields.IntField(unique=True)
    is_superadmin = fields.BooleanField(default=False)
