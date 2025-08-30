from fastapi import APIRouter, HTTPException
from database.db_connection import users_collection, jobs_collection
from model.recommender import recommend_jobs_for_user
from bson import ObjectId

router = APIRouter()

@router.get("/recommend/{user_id}")
def get_recommendations(user_id: str):
    # Step 1: Validate ObjectId
    try:
        user_obj_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user_id format")

    # Step 2: Fetch user
    user = users_collection.find_one({"_id": user_obj_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Step 3: Get skills & profile
    user_skills = user.get("skills", [])
    
    # Step 4: Fetch jobs
    jobs = list(jobs_collection.find())
    if not jobs:
        return {
            "user_id": user_id,
            "message": "No job listings available right now.",
            "recommendations": []
        }

    # Step 5: Generate recommendations
    recommendations = recommend_jobs_for_user(user_skills, jobs)

    # Normal case
    if not recommendations:
        return {
            "user_id": user_id,
            "message": "No recommendations found at this time. Try updating your skills/profile.",
            "recommendations": []
        }

    return {
        "user_id": user_id,
        "message": "Success",
        "recommendations": recommendations
    }