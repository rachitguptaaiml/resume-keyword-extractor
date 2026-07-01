# Resume Keyword Extractor and Matcher
A Python-based tool that extracts relevant keywords from resumes and matches them with job openings using NLP techniques.

## Tech Stack
* Python
* scikit-learn for TF-IDF vectorization and cosine similarity computation
* pandas for data manipulation

## Problem Statement
Extracting the right keywords from a resume to match with job openings can be time-consuming. This project aims to develop an efficient tool that can automate this process.

## Features
* Extracts relevant keywords from resumes using TF-IDF vectorization
* Computes cosine similarity between extracted keywords and job descriptions for matching

## Setup/Run Instructions
1. Clone the repository: `git clone https://github.com/your-username/resume-keyword-extractor.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run the script: `python main.py`

## Sample Output
Extracted Keywords:
Keyword 1: [0.0123456789, 0.013456789, ...]
Keyword 2: [0.024567890, 0.025678901, ...]

Similarities between job descriptions and extracted keywords:
Job Description 1: 0.85
Job Description 2: 0.92

## What I Learned
This project taught me the importance of NLP techniques in automating tasks that were previously done manually. By leveraging scikit-learn's TF-IDF vectorization and cosine similarity computation, we can efficiently extract relevant keywords from resumes and match them with job openings. This experience has also shown me the value of writing clean, readable code and documenting my processes effectively.