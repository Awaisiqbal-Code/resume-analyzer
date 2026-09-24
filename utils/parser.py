"""Utilities for resume text extraction."""

import pdfplumber
from docx import Document
import streamlit as st


def extract_pdf_text(uploaded_file):
    """Extract text from a PDF file."""
    text = ""
    try:
        uploaded_file.seek(0)
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as exc:  # pragma: no cover - runtime error reporting
        st.error(f"Error reading PDF: {exc}")
    return text


def extract_docx_text(uploaded_file):
    """Extract text from a DOCX file."""
    text = ""
    try:
        uploaded_file.seek(0)
        document = Document(uploaded_file)
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
    except Exception as exc:  # pragma: no cover - runtime error reporting
        st.error(f"Error reading DOCX: {exc}")
    return text


def extract_text(uploaded_file):
    """Detect the uploaded resume type and extract text."""
    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()
    if file_name.endswith(".pdf"):
        return extract_pdf_text(uploaded_file)
    if file_name.endswith(".docx"):
        return extract_docx_text(uploaded_file)

    st.error("Only PDF and DOCX files are supported.")
    return ""
