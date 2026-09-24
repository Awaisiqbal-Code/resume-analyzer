"""
=========================================================
jobs.py

Purpose:
--------
Store predefined job roles, descriptions and
required skills.

The application uses:

1. Job Description
   -> For ML Model Prediction

2. Required Skills
   -> For Skill Matching

Author:
AI Resume Analyzer
=========================================================
"""

JOB_DATABASE = {

    "Machine Learning Engineer": {

        "description": """
Machine Learning Engineer

Required Skills:
Python
Machine Learning
Deep Learning
TensorFlow
PyTorch
Scikit-learn
SQL
Pandas
NumPy
Statistics
Data Visualization
Docker
Git
AWS

Education:
Bachelor's or Master's degree in Computer Science,
Artificial Intelligence,
Data Science.

Responsibilities:
Build ML models.
Deploy AI solutions.
Feature Engineering.
Model Evaluation.
""",

        "skills": [

            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "Scikit-learn",
            "SQL",
            "Pandas",
            "NumPy",
            "Statistics",
            "Docker",
            "Git",
            "AWS"

        ]
    },

    "Data Scientist": {

        "description": """
Data Scientist

Required Skills:
Python
Machine Learning
Statistics
Pandas
NumPy
SQL
Power BI
Tableau
Matplotlib
Seaborn
Data Cleaning
Feature Engineering

Education:
Bachelor's or Master's degree.

Responsibilities:
Analyze data.
Build predictive models.
Generate reports.
Business insights.
""",

        "skills": [

            "Python",
            "Machine Learning",
            "Statistics",
            "Pandas",
            "NumPy",
            "SQL",
            "Power BI",
            "Tableau",
            "Matplotlib",
            "Seaborn",
            "Data Cleaning",
            "Feature Engineering"

        ]
    },

    "AI Engineer": {

        "description": """
AI Engineer

Required Skills:
Python
TensorFlow
PyTorch
Transformers
LLMs
Computer Vision
NLP
Deep Learning
Machine Learning
Docker
Linux
Git

Responsibilities:
Develop AI applications.
Train deep learning models.
Deploy AI systems.
""",

        "skills": [

            "Python",
            "TensorFlow",
            "PyTorch",
            "Transformers",
            "LLMs",
            "Computer Vision",
            "NLP",
            "Deep Learning",
            "Machine Learning",
            "Docker",
            "Linux",
            "Git"

        ]
    },

    "Python Developer": {

        "description": """
Python Developer

Required Skills:
Python
Flask
Django
REST API
OOP
SQL
Git
HTML
CSS
JavaScript

Responsibilities:
Backend Development.
API Development.
Debugging.
Database Management.
""",

        "skills": [

            "Python",
            "Flask",
            "Django",
            "REST API",
            "OOP",
            "SQL",
            "Git",
            "HTML",
            "CSS",
            "JavaScript"

        ]
    },

    "Data Analyst": {

        "description": """
Data Analyst

Required Skills:
Excel
SQL
Python
Power BI
Tableau
Statistics
Data Cleaning
Visualization

Responsibilities:
Analyze data.
Create dashboards.
Prepare reports.
""",

        "skills": [

            "Excel",
            "SQL",
            "Python",
            "Power BI",
            "Tableau",
            "Statistics",
            "Data Cleaning",
            "Visualization"

        ]
    }

}