from pymongo import MongoClient

def get_databases():
    client = MongoClient("mongodb+srv://<connection_string>/?retryWrites=true&w=majority")
    db = client.test

    dbs = client.admin.command({"listDatabases": 1})
    for database in dbs["databases"]:
        print(database)

get_databases()
