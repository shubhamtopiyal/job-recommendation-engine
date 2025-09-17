# Job Recommendation Engine

A personalised **Job Recommendation Engine** built with **FastAPI**, **MongoDB**, and **Scikit-learn**.
It suggests jobs to candidates based on their skills using **TF-IDF and Cosine Similarity**.


## 🚀 Features
- Content-based job recommendations (skills → jobs)
- FastAPI backend with REST API endpoints
- MongoDB as the data source for users & job posts
- Real-time recommendations based on candidate profile

## 🛠️ Tech Stack
- Backend: FastAPI (Python)
- Database: MongoDB
- Machine Learning: Scikit-learn (TF-IDF, Cosine Similarity)

## ⚙️ Workflow

- User adds skills in the portal.
- React frontend sends request → /recommend/{user_id}.
- FastAPI backend fetches user profile + job posts from MongoDB.
- Recommender Engine (TF-IDF + Cosine Similarity) finds top matches.
- Backend returns JSON with recommended jobs.
- Frontend displays jobs to the user.

## 📂 Project Structure
```bash
job-recommendation-engine/
│── main.py                 # FastAPI entry point
│── routes/                 # API routes
│   └── recommendation.py   # Job recommendation endpoint
│── model/                  
│   └── recommender.py      # TF-IDF + Cosine similarity logic
│── database/               
│   └── db_connection.py    # MongoDB connection
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

## 🔮 Future Enhancements
- Hybrid recommendations (skills + job history)
- Resume parsing for auto-skill extraction
- Deployment to cloud (Render, Vercel, or AWS)

## 🌐 Live Demo:
- Try the app here 👉 [Deployed Link](https://job-recommendation-engine-92pw.onrender.com)  


## 📧 Contact:
Developed by Shubham Topiyal  

📨 shubhamtopiyal0786@gmail.com 

📌 Feel free to reach out for feedback or collaboration!  
