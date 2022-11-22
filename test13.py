import pymongo
client = pymongo.MongoClient("mongodb+srv://Medata:8kPyvqDvfYWVKN4k@cluster0.zr2e2ig.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"mukesh",
    "lastname":"kumar",
    "email_id":"sizalmuky@gmail.com"

}
d={
    "name":"mukesh",
    "lastname":"kumar",
    "email_id":"sizalmuky@gmail.com"

}
d={
    "name":"mukesh",
    "lastname":"kumar",
    "email_id":"sizalmuky@gmail.com"

}
d={
    "name":"mukesh",
    "lastname":"kumar",
    "email_id":"sizalmuky@gmail.com"

}
d={
    "name":"mukesh",
    "lastname":"kumar",
    "email_id":"sizalmuky@gmail.com"

}
d={
    "name":"mukesh",
    "lastname":"kumar",
    "email_id":"sizalmuky@gmail.com"

}


db1=client['mongotest']
coll=db['test']
coll.insert_one(d)