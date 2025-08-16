# Defines our FastAPI backend for serving job recommendations based on the user’s skills stored in MongoDB.

from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
from model.recommender import recommend_jobs_for_user
from pymongo import MongoClient
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

# Allow frontend requests (React)
#This allows React frontend to fetch data from your FastAPI backend — otherwise, it’ll be blocked due to CORS (Cross-Origin Resource Sharing).

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use frontend URL"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to MongoDB
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client["job_portal"]  # DB name


# Simple test route to verify the backend is working
@app.get("/")
def read_root():
    return {"message": "Job Recommendation API is running!"}


# Endpoint to get job recommendations for a user
@app.get("/recommend/{user_id}")
async def recommend_jobs(user_id: str):
    # Route accepts a user_id (from MongoDB) and fetches the corresponding user.
    # Converts user_id to ObjectId because MongoDB stores _id as ObjectId, not plain string.
    # If user is not found → returns 404 Not Found.
    try:
        user = await db["users"].find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Get user's skills 
        # Pulls the skills field from the user document.
        user_skills = user.get("skills", [])
        if not user_skills:
            raise HTTPException(status_code=400, detail="No skills found in user profile")

        # Fetch all jobs
        # Pulls all job documents from the jobs collection.
        # Asynchronously iterates over the cursor and adds them to a Python list.
        jobs_cursor = db["jobs"].find({})
        jobs = []
        async for job in jobs_cursor:
            job["_id"] = str(job["_id"])  # Convert ObjectId to string
            jobs.append(job)

        # Get top recommended jobs using your model
        # Calls your TF-IDF / Cosine model (defined separately) with user skills and job data
        # Returns the top N matching jobs as a JSON list to the frontend
        recommended_jobs = recommend_jobs_for_user(user_skills, jobs)
        return {"recommendations": recommended_jobs}

    # If any unhandled error occurs, return HTTP 500 with error message (for debugging).
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#EOC