from pymongo import MongoClient
from pprint import pprint
import config
client = MongoClient(config.MongoClient)


db = client.customers
collection = db.addressCollection


# Loop for entries
while True:
    names = input("Customer's Name(s): ")
    if names == "quit":
        break
    address = input("Customer's Address: ")
    material = input("Pipe material: ")

# Dictionary Creation and Upload
    document1 = {
    "name":names,
    "address":address,
    "material":material
}
    
    collection.insert_one(document1)
    pprint("Item Uploaded Successfully")






