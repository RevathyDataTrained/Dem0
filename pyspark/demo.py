
import pymongo
import requests
import dns
def function():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    response=response.json() 
    print(response)
   
    myclient = pymongo.MongoClient("mongodb+srv://revathy:revathy%40job@cluster123.hh0pp.mongodb.net/test")
    db = myclient["Apidb"]
    collection = db["Apicollection"]
    print(myclient.list_database_names())
    x=collection.insert_one(response)
    print(x)
   
    
function()    