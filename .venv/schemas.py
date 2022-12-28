from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True) #only for return
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchma(Schema):
    name = fields.Str()
    price = fields.Str()
    
class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    
