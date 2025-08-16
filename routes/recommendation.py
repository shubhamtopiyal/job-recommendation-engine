# routes/recommendation.py

from fastapi import APIRouter, HTTPException
from database.db_connection import users_collection, jobs_collection
from model.recommender import recommend_jobs_for_user
from bson import ObjectId

router = APIRouter()

@router.get("/recommend/{user_id}")
async def get_recommendations(user_id: str):
    # Step 1: Validate ObjectId
    try:
        user_obj_id = ObjectId(user_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid user_id format")

    # Step 2: Fetch user
    user = users_collection.find_one({"_id": user_obj_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Step 3: Get skills from user document
    user_skills = user.get("skills", [])
    if not user_skills:
        raise HTTPException(status_code=400, detail="No skills found in user profile")

    # Step 4: Fetch jobs from DB
    jobs = list(jobs_collection.find())
    if not jobs:
        raise HTTPException(status_code=404, detail="No job listings found")

    # Step 5: Get recommendations
    recommendations = recommend_jobs_for_user(user_skills, jobs)

    return {
        "user_id": user_id,
        "recommendations": recommendations
    }