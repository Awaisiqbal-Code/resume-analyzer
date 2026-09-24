"""
=========================================================
parser.py

Purpose:
--------
This module extracts text from uploaded resumes.

Supported File Types:
1. PDF (.pdf)
2. Microsoft Word (.docx)

The extracted text is returned as a single string.

Author:
AI Resume Analyzer Project
=========================================================
"""

import pdfplumber
from docx import Document
import streamlit as st


def extract_pdf_text(uploaded_file):
    """
    Extract text from a PDF file.

    Parameters
    ----------
    uploaded_file : UploadedFile
        File uploaded through Streamlit.

    Returns
    -------
    str
        Extracted text from all pages.
    """

    text = ""

    try:

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:

        st.error(f"Error reading PDF: {e}")

    return text


def extract_docx_text(uploaded_file):
    """
    Extract text from a DOCX file.

    Parameters
    ----------
    uploaded_file : UploadedFile

    Returns
    -------
    str
        Complete document text.
    """

    text = ""

    try:

        document = Document(uploaded_file)

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"

    except Exception as e:

        st.error(f"Error reading DOCX: {e}")

    return text


def extract_text(uploaded_file):
    """
    Automatically detect the uploaded file type
    and call the correct extraction function.

    Parameters
    ----------
    uploaded_file : UploadedFile

    Returns
    -------
    str
        Resume text
    """

    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):

        return extract_pdf_text(uploaded_file)

    elif file_name.endswith(".docx"):

        return extract_docx_text(uploaded_file)

    else:

        st.error("Only PDF and DOCX files are supported.")

        return ""