"""
=========================================================
AI Resume Analyzer
Author : Shan Ali

This Streamlit application allows users to:

1. Upload Resume (PDF/DOCX)
2. Select Job Role
3. Predict ATS Match Score
4. Show Matched Skills
5. Show Missing Skills
6. Give Resume Suggestions

=========================================================
"""

# =========================================================
# Import Libraries
# =========================================================

import streamlit as st

from utils.parser import extract_text
from utils.jobs import JOB_DATABASE

from utils.predictor import (
    predict_resume_score,
    compare_skills,
    generate_strengths,
    generate_suggestions
)

# =========================================================
# Streamlit Page Configuration
# =========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# =========================================================
# Custom CSS
# =========================================================

st.markdown(
    """
    <style>

    .main{
        padding-top:20px;
    }

    .title{
        text-align:center;
        color:#1E88E5;
        font-size:40px;
        font-weight:bold;
    }

    .subtitle{
        text-align:center;
        color:gray;
        font-size:18px;
    }

    .box{
        background-color:#F4F6F6;
        padding:20px;
        border-radius:10px;
        margin-top:15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# Application Title
# =========================================================

st.markdown(
    "<h1 class='title'>📄 AI Resume Analyzer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Upload your Resume and Check ATS Match Score</p>",
    unsafe_allow_html=True
)

st.divider()

# =========================================================
# Sidebar
# =========================================================

st.sidebar.title("📌 Instructions")

st.sidebar.info(
"""
1. Upload Resume

2. Select Target Job

3. Click Analyze

4. View ATS Score

5. Check Missing Skills

6. Improve Resume
"""
)

st.sidebar.success("Supported Formats")

st.sidebar.write("✔ PDF")

st.sidebar.write("✔ DOCX")

# =========================================================
# Main Layout
# =========================================================

left_col, right_col = st.columns([2,1])

# =========================================================
# LEFT COLUMN
# =========================================================

with left_col:

    st.subheader("📂 Upload Resume")

    uploaded_file = st.file_uploader(

        "Choose Resume",

        type=["pdf","docx"]

    )

# =========================================================
# RIGHT COLUMN
# =========================================================

with right_col:

    st.subheader("💼 Select Target Job")

    selected_job = st.selectbox(

        "Choose Job Role",

        list(JOB_DATABASE.keys())

    )

# =========================================================
# Analyze Button
# =========================================================

st.divider()

analyze = st.button(

    "🔍 Analyze Resume",

    use_container_width=True

)

# =========================================================
# Stop if Resume not Uploaded
# =========================================================

if analyze and uploaded_file is None:

    st.warning("Please upload your resume first.")

    st.stop()

# =========================================================
# Extract Resume Text
# =========================================================

if analyze:

    with st.spinner("Reading Resume..."):

        resume_text = extract_text(uploaded_file)

    if resume_text.strip() == "":

        st.error("Unable to extract text from Resume.")

        st.stop()

    st.success("Resume Uploaded Successfully!")

    # Save for Part 2
    st.success("✅ Resume Uploaded Successfully!")

    # ==========================================
    # Get Selected Job Information
    # ==========================================

    job_description = JOB_DATABASE[selected_job]["description"]

    required_skills = JOB_DATABASE[selected_job]["skills"]

    # ==========================================
    # Predict ATS Score
    # ==========================================

    with st.spinner("Analyzing Resume..."):

        score = predict_resume_score(
            resume_text,
            job_description
        )

    # ==========================================
    # Compare Skills
    # ==========================================

    matched_skills, missing_skills = compare_skills(

        resume_text,

        required_skills

    )

    strengths = generate_strengths(score)

    suggestions = generate_suggestions(missing_skills)

    # ==========================================
    # ATS Score
    # ==========================================

    st.divider()

    st.header("📊 ATS Resume Analysis")

    st.metric(

        "ATS Match Score",

        f"{score}%"

    )

    st.progress(score / 100)

    # ==========================================
    # Resume Status
    # ==========================================

    if score >= 80:

        st.success("🟢 Excellent Match")

    elif score >= 60:

        st.warning("🟡 Good Match")

    else:

        st.error("🔴 Needs Improvement")

    # ==========================================
    # Skills Section
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if matched_skills:

            for skill in matched_skills:

                st.success(skill)

        else:

            st.info("No matched skills found.")

    with col2:

        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:

                st.error(skill)

        else:

            st.success("No missing skills.")

    # ==========================================
    # Resume Strengths
    # ==========================================

    st.divider()

    st.subheader("💪 Resume Strengths")

    for strength in strengths:

        st.success(strength)

    # ==========================================
    # Suggestions
    # ==========================================

    st.divider()

    st.subheader("💡 Suggestions")

    if suggestions:

        for suggestion in suggestions:

            st.warning(suggestion)

    else:

        st.success("Excellent Resume!")

    # ==========================================
    # Resume Preview
    # ==========================================

    st.divider()

    with st.expander("📄 View Extracted Resume"):

        st.text_area(

            "Resume Text",

            resume_text,

            height=350

        )
        