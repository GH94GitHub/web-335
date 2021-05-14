#=================================
# Title: User-Service
# Author: George Henderson
# Date: 14 May 2021
# Description: Uses pymongo to insert a user
# into a local mongo db.
#=================================

from pymongo import MongoClient
import datetime
import pprint

client = MongoClient('localhost', 27017)
db = client.web335

user = {
    "first_name": "Jeff",
    "last_name": "Jefferson",
    "email": "jJefferson@email.com",
    "employee_id": "01005",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id
print(user_id)
pprint.pprint(db.users.find_one({"employee_id":"01005"}))