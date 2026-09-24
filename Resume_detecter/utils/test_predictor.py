from utils.predictor import predict_resume_score

resume = """
Python
Machine Learning
TensorFlow
SQL
"""

job = """
Machine Learning Engineer

Python

TensorFlow

SQL

Docker

AWS
"""

score = predict_resume_score(resume, job)

print(score)