# AI Resume Analyzer

A professional resume screening and ATS match scoring application built with Streamlit.

## Overview
This project analyzes a candidate resume against a selected job description and produces:
- ATS match score
- matched skills
- missing skills
- resume strengths
- improvement suggestions

It accepts PDF and DOCX resume uploads and supports free deployment on Streamlit Community Cloud.

## Project Structure

```text
resume-analyzer/
├── app.py                 # Streamlit application entry point
├── requirements.txt       # Python dependencies
├── .gitignore            # Ignore local/cache files
├── .streamlit/
│   └── config.toml       # Community Cloud configuration
├── README.md             # Project documentation
├── models/               # Root-level model folder (preferred)
│   ├── resume_match_model.pkl
│   └── tfidf.pkl
├── utils/
│   ├── __init__.py
│   ├── jobs.py           # Job descriptions and required skills
│   ├── parser.py         # PDF/DOCX extraction logic
│   ├── predictor.py      # Model loading and prediction functions
│   ├── preprocessing.py # Text cleaning and NLP preprocessing
│   └── test_predictor.py # Quick sanity check script
└── Resume_detecter/      # Legacy project directory retained for compatibility
```

## Features
- Upload a resume in PDF or DOCX format
- Select a target job role
- Evaluate ATS compatibility score
- Compare matched vs missing skills
- Generate actionable recommendations
- Ready for Streamlit Community Cloud deployment

## Local Development
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

## Streamlit Community Cloud Deployment
1. Push this repository to GitHub
2. Open Streamlit Community Cloud
3. Select the repository and branch
4. Choose the file `app.py` as the app entry point
5. Deploy

The project is configured to run without needing paid services or external cloud infrastructure.

## Notes
- The application preserves the original resume-analyzer functionality.
- Model files are loaded from the preferred root `models/` folder and also fall back to the legacy `Resume_detecter/models/` path for compatibility.
- Unnecessary local cache and editor files are excluded via `.gitignore`.
