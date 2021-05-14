#=================================
# Title: User-Update
# Author: George Henderson
# Date: 14 May 2021
# Description: Uses pymongo to update a user
# in a local mongo db.
#=================================

from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335

db.users.update_one(
    {
        "employee_id": "01005"
    },
    {
        "$set": {
            "email":"gahenderson@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one(
    {"employee_id":"01005"}
))