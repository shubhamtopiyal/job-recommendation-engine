from database.db_connection import users_collection

print("Starting test...")

user = users_collection.find_one()
print("User found:", user)
print("Test completed successfully.")