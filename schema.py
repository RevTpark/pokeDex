from marshmallow import Schema, fields

class TypeQueryScehma(Schema):
    type1 = fields.Str(required=True)
    type2 = fields.Str()
