import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema
#Blueprint is used to divide an API into multiple segments
blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")

@blp.response(200, StoreSchema)
class Stores(MethodView):
    def get(self, store_id):
     try:
        return stores[store_id]
     except KeyError:
         abort(404, message="Store not found")
    
    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return {"stores": stores.values()}
    
    @blp.arguments(StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=("Store already exists."))
        store_id = uuid.uuid4().hex
        #dictionary of 2 keys, name and items, name is taken from json
        store={**store_data, "id": store_id}
        stores[store_id] = store
        return store 

