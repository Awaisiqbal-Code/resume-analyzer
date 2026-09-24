"""
=========================================================
predictor.py

Purpose:
--------
This module loads the trained model and predicts
the resume match score.

It also performs simple skill matching and generates
basic improvement suggestions.

Author:
AI Resume Analyzer Project
=========================================================
"""

# ============================================
# Import Libraries
# ============================================

import os
import ast
import joblib

from utils.preprocessing import clean_text

# ============================================
# Load Saved Model and TF-IDF
# ============================================

# ============================================
# Load Trained Model and TF-IDF Vectorizer
# ============================================

import os
import joblib

# Get project root directory
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model folder
MODEL_DIR = os.path.join(PROJECT_DIR, "models")

# Model files
MODEL_PATH = os.path.join(MODEL_DIR, "resume_match_model.pkl")
TFIDF_PATH = os.path.join(MODEL_DIR, "tfidf.pkl")

# Load saved model
model = joblib.load(MODEL_PATH)

# Load saved TF-IDF vectorizer
tfidf = joblib.load(TFIDF_PATH)

print("✅ Resume Match Model Loaded Successfully")

print("✅ TF-IDF Vectorizer Loaded Successfully")
# ============================================
# Predict Match Score
# ============================================

def predict_resume_score(resume_text, job_description):

    combined_text = resume_text + " " + job_description

    cleaned_text = clean_text(combined_text)

    vector = tfidf.transform([cleaned_text])

    score = model.predict(vector)[0]

    score = max(0, min(score, 1))

    return round(score * 100, 2)

# ============================================
# Convert Skills String to List
# ============================================

def convert_skill_string(skill_text):

    
    if not skill_text:
        return []

    try:

        skills = ast.literal_eval(skill_text)

        if isinstance(skills, list):

            return [str(skill).strip().lower() for skill in skills]

    except:

        pass

    return []

# ============================================
# Find Matched and Missing Skills
# ============================================

def compare_skills(resume_text, required_skills):

    resume_text = resume_text.lower()

    matched = []

    missing = []

    for skill in required_skills:

        if skill.lower() in resume_text:

            matched.append(skill)

        else:

            missing.append(skill)

    return matched, missing

# ============================================
# Generate Suggestions
# ============================================

def generate_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:

        suggestions.append(f"Learn or add '{skill}' to your resume if you have experience.")

    return suggestions

# ============================================
# Resume Strengths
# ============================================

def generate_strengths(score):

    strengths = []

    if score >= 80:

        strengths.append("Excellent overall profile.")

        strengths.append("Resume matches most required skills.")

        strengths.append("Strong ATS compatibility.")

    elif score >= 60:

        strengths.append("Good resume with relevant technical skills.")

        strengths.append("Can be improved by adding missing skills.")

    else:

        strengths.append("Resume needs improvement.")

        strengths.append("Consider adding projects, certifications and technical skills.")

    return strengths