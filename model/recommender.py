# Recommendation Logic
# This code is part of a job recommendation engine that uses TF-IDF and cosine similarity to recommend jobs based on user skills.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs_for_user(user_skills, jobs, top_n=5):
    # Clean and validate skills
    user_skills = [skill.strip().lower() for skill in user_skills if skill.strip()]
    if not user_skills:
        return []

    # Prepare user document
    user_doc = " ".join(user_skills)

    # Prepare job documents
    job_docs = [
        " ".join(skill.strip().lower() for skill in job.get("requiredSkills", []) if skill.strip())
        for job in jobs
    ]

    # Combine all documents
    all_docs = [user_doc] + job_docs

    # Generate TF-IDF matrix
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(all_docs)

    if tfidf_matrix.shape[0] < 2:
        return [] # Not enough data to compare

    # Compute cosine similarity between user and all jobs
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Get top N jobs
    top_indices = cosine_sim.argsort()[-top_n:][::-1]

    recommendations = []
    for i in top_indices:
        score = float(cosine_sim[i])
        if score == 0.0:
            continue  # skip irrelevant jobs
        job = jobs[i].copy()  # avoid mutating original
        job["_id"] = str(job["_id"])  # convert ObjectId to str
        job["score"] = round(score, 3)
        recommendations.append(job)

    return recommendations
