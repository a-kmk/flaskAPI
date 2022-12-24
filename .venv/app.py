import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores,items

#in most APIs you store the data in a DB
app = Flask(__name__)

#in JSON everything has to be inside lists or numbers, the advantage with JSON is that it it's a string of text.
#main reason for using db instead of a python list is that lists dont persist


# the endpoint is the /store, the function
# associated with that endpoint is get_stores
@app.get("/store") #http:127.0.0.1:5000/store
def get_stores():
    return {"stores" :list(stores.values())}

@app.get("/store/<string:store_id>")
def get_store(name):
    try:
        return stores[store_id]
    except KeyError:
         abort(404, message="Store not found")

@app.get("/item/<string:item_id>")
def get_item_in_store(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")
    
@app.post("/store")
def create_store():
    store_data=request.get_json()
    store_id = uuid.uuid4().hex
    #dictrionary of 2 keys, name and items, name is taken from json
    store={**store_data, "id": store_id}
    stores[store_id] = store
    #200 means ok, but 201 means i accepted data and will create the store
    return store, 201

#endpoint the client requests is dynamic and in the URL
@app.post("/item")
def create_item(name):
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
         abort(404, message="Store not found")
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] =  item
    
    return item, 201

@app.get("/item")
def get_all_items():
    return {"items" :list(items.values())}

#what happens if two stores have the same name
#using query string parameters and headers are also other ways






