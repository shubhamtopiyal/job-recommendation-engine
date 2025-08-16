# MondoDB Connection Module
# This module establishes a connection to the MongoDB database and provides access to the collections.

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# storing MongoDB URL in a variable
MONGODB_URI = os.getenv("MONGODB_URI")

# Creating MongoDB client
client = MongoClient(MONGODB_URI)

# Accessing database
db = client["job_portal"]

# Accessing collections
users_collection = db["users"]
jobs_collection = db["jobposts"]

#EOC