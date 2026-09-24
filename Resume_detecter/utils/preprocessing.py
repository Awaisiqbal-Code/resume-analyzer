"""
=========================================================
preprocessing.py

Purpose:
--------
This module cleans resume and job description text
before prediction.

The preprocessing steps are the SAME as those used
during model training.

Author:
AI Resume Analyzer Project
=========================================================
"""

# ==============================
# Import Required Libraries
# ==============================

import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ==============================
# Download NLTK Resources
# (Only the first time)
# ==============================

resources = {
    "punkt": "tokenizers/punkt",
    "stopwords": "corpora/stopwords",
    "wordnet": "corpora/wordnet"
}

for resource_name, resource_path in resources.items():

    try:

        nltk.data.find(resource_path)

    except LookupError:

        nltk.download(resource_name)

# ==============================
# Initialize NLP Objects
# ==============================

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))

# ==============================
# Text Cleaning Function
# ==============================

def clean_text(text):
    """
    Clean raw resume/job text.

    Steps
    -----
    1. Convert to lowercase
    2. Remove URLs
    3. Remove numbers
    4. Remove punctuation
    5. Tokenize
    6. Remove stopwords
    7. Lemmatize
    8. Join words back into text

    Parameters
    ----------
    text : str

    Returns
    -------
    str
    """

    if text is None:
        return ""

    # Convert to string
    text = str(text)

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove Email Addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove Phone Numbers
    text = re.sub(r"\+?\d[\d\s()-]{7,}", " ", text)

    # Remove Digits
    text = re.sub(r"\d+", " ", text)

    # Remove Special Characters
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove Extra Spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenization
    tokens = nltk.word_tokenize(text)

    # Stopword Removal + Lemmatization
    cleaned_tokens = []

    for word in tokens:

        if word not in stop_words:

            cleaned_word = lemmatizer.lemmatize(word)

            cleaned_tokens.append(cleaned_word)

    return " ".join(cleaned_tokens)