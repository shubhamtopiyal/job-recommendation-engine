# FastAPI app entry point
# This file sets up the FastAPI application, and defines API endpoints

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes.recommendation import router as recommendation_router

app = FastAPI()

# Allow React frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with actual domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(recommendation_router)

@app.get("/")
def read_root():
    return {"message": "Job Recommendation API is running!"}