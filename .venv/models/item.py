from db import db 

#mapping between row in a table and python class/object
class ItemModel(db.Model):
    __tablename__ = "items"
    
    #define columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    
    #one-to-many
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    # when we have an myitem.store will return the right store
    store = db.relationship("StoreModel", back_populates="items")
    