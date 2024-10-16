from marshmallow import Schema, fields, validate, post_load
from app.models.user import User


class UserMap(Schema):
    id = fields.Integer(dump_only=True)
    firstname: str = fields.String(required=True)
    lastname: str = fields.String(required=True)
    email: str = fields.String(required=True, validate=validate.Email())
    password: str = fields.String(load_only=True)
    role: int = fields.Integer(required=True)
    
    @post_load
    def bind_user(self, data, **kwargs):
        return User(**data)