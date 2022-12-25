from tortoise.models import Model
from tortoise import fields


class Sections(Model):
    id = fields.IntField(pk=True)
    dir_name = fields.TextField()
    name = fields.TextField()

class Files(Model):
    id = fields.IntField(pk=True)
    file_name = fields.TextField()
    name = fields.TextField()
    section = fields.ForeignKeyField("models.Sections",
                                     on_delete=fields.CASCADE,
                                     related_name="files")
