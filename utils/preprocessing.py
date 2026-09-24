"""Model loading and scoring utilities for the resume analyzer."""

from __future__ import annotations

import ast
from pathlib import Path

import joblib

from utils.preprocessing import clean_text

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_SEARCH_DIRS = [
    BASE_DIR / "models",
    BASE_DIR / "Resume_detecter" / "models",
]


def _resolve_model_path(filename: str) -> Path:
    for directory in MODEL_SEARCH_DIRS:
        candidate = directory / filename
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"Model file not found: {filename}")


MODEL_PATH = _resolve_model_path("resume_match_model.pkl")
TFIDF_PATH = _resolve_model_path("tfidf.pkl")

model = joblib.load(str(MODEL_PATH))
tfidf = joblib.load(str(TFIDF_PATH))


def predict_resume_score(resume_text, job_description):
    combined_text = resume_text + " " + job_description
    cleaned_text = clean_text(combined_text)
    vector = tfidf.transform([cleaned_text])
    score = model.predict(vector)[0]
    score = max(0, min(score, 1))
    return round(score * 100, 2)


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


def generate_suggestions(missing_skills):
    suggestions = []
    for skill in missing_skills:
        suggestions.append(f"Learn or add '{skill}' to your resume if you have experience.")
    return suggestions


def generate_strengths(score):
    strengths = []
    if score >= 80:
        strengths.extend([
            "Excellent overall profile.",
            "Resume matches most required skills.",
            "Strong ATS compatibility.",
        ])
    elif score >= 60:
        strengths.extend([
            "Good resume with relevant technical skills.",
            "Can be improved by adding missing skills.",
        ])
    else:
        strengths.extend([
            "Resume needs improvement.",
            "Consider adding projects, certifications and technical skills.",
        ])
    return strengths


def convert_skill_string(skill_text):
    if not skill_text:
        return []
    try:
        skills = ast.literal_eval(skill_text)
        if isinstance(skills, list):
            return [str(skill).strip().lower() for skill in skills]
    except Exception:
        pass
    return []
