# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. . 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals'
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    def getRecordCount(self):
        # Counts the current documents and adds 1
        count = self.collection.count_documents({})
        return count + 1
            
    # implement the C in CRUD. 
    def create(self, data):
        if data is not None:
            try:
                # Update the data with the next available record ID
                next_id = self.getRecordCount()
                data['record_id'] = next_id
                
                # Insert the data
                self.database.animals.insert_one(data)  # data should be dictionary
                
                # Return True if successful
                return True
            except Exception as e:
                print (f"An error occurred: {e}")
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # implement the R in CRUD.
    def read(self, data):
        if data is not None:
            # Use find() to retrieve all matching docs
            cursor = self.collection.find(data)
            
            # Convert the cursor to a list and return it
            return list(cursor)
        else:
            raise Exception("Nothing to search, data parameter is empty")
            
    # implement the U in CRUD
    def update(self, query, data):
        if data is not None:
            # update_many allows updating multiple docs if the query matches more than one.
            # using $set to ensure only the fields passed get updated rather than overwriting the whole document.
            result = self.collection.update_many(query, {"$set": data})
            
            # return the number of objects modified
            return result.modified_count
        else:
            raise Exception("Nothing to update")
    
    # implement the D in CRUD
    def delete(self, query):
        if query is not None:
            # delete_many removes all docs matching the query criteria
            result = self.collection.delete_many(query)
            
            # return number of objects removed
            return result.deleted_count
        else:
            raise Exception("Nothing to delete")