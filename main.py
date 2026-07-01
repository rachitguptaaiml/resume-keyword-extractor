import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ResumeKeywordExtractor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def extract_keywords(self, resume_text):
        return self.vectorizer.fit_transform([resume_text]).toarray()[0]

    def match_keywords_with_jobs(self, job_descs):
        vectorized_job_descs = self.vectorizer.transform(job_descs)
        similarities = cosine_similarity(vectorized_job_descs)
        return similarities

def main():
    extractor = ResumeKeywordExtractor()

    # Sample synthetic resume data
    resumes = [
        "Software engineer with expertise in Python and machine learning.",
        "Data scientist with experience in pandas, NumPy, and scikit-learn."
    ]

    # Sample synthetic job descriptions
    jobs = [
        "We are looking for a software engineer with experience in Python and web development.",
        "A data scientist with expertise in pandas, NumPy, and machine learning is required."
    ]

    extracted_keywords = [extractor.extract_keywords(resume) for resume in resumes]
    similarities = extractor.match_keywords_with_jobs(jobs)

    print("Extracted Keywords:")
    for i, keyword in enumerate(extracted_keywords[0]):
        print(f"Keyword {i+1}: {keyword}")

    print("\nSimilarities between job descriptions and extracted keywords:")
    for i, similarity in enumerate(similarities):
        print(f"Job Description {i+1}: {similarity:.2f}")

if __name__ == "__main__":
    main()