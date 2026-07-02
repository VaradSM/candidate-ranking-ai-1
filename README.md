# AI-Powered Candidate Ranking System

## Overview

This project was developed for the Redrob Intelligent Candidate Discovery & Ranking Challenge.

The objective is to rank candidates against a job description using a hybrid AI-driven ranking approach that combines:

- Semantic Matching
- Career Relevance
- Behavioral Signals
- Location Fit

The system processes 100,000 candidate profiles and returns the Top 100 most relevant candidates.

---

## Project Architecture

Job Description

       |

       v
Semantic Embedding Generation
       
       |
       
       v
Candidate Embedding Search
       
       |
       
       v
Feature Engineering
       
       |
       
       +--> Career Score
       
       +--> Behavior Score
       
       +--> Location Score
       
       |
       
       v
       
Weighted Scoring Engine
       
       |
       
       v
       
Final Ranking
      
       |
       
       v
       
Top 100 Candidates

---

## Methodology

### 1. Semantic Similarity (50%)

Sentence embeddings are generated using:

BAAI/bge-small-en-v1.5

Candidate profiles and the job description are converted into dense vector representations.

Cosine similarity is used to measure semantic relevance.

---

### 2. Career Score (30%)

Career relevance is evaluated using:

- Current Title
- Career History
- AI/ML Experience
- Retrieval & Ranking Experience
- NLP / Search / Recommendation Systems Exposure

Examples of preferred roles:

- AI Engineer
- ML Engineer
- NLP Engineer
- Search Engineer
- Applied ML Engineer
- Senior AI Engineer

---

### 3. Behavioral Score (15%)

Behavioral signals are extracted from:

- Recruiter Response Rate
- Open To Work Status
- Last Active Date
- Interview Completion Rate
- Saved By Recruiters
- Profile Completeness

These features improve recruiter-facing relevance.

---

### 4. Location Score (5%)

Candidates are rewarded if they:

- Are located in preferred hiring cities
- Are willing to relocate
- Match job location preferences

---

## Final Ranking Formula

Final Score =
0.50 × Semantic Similarity
+ 0.30 × Career Score
+ 0.15 × Behavior Score
+ 0.05 × Location Score

---

## Tech Stack

- Python
- NumPy
- Pandas
- Sentence Transformers
- BGE Embeddings
- Scikit-Learn

---

## Dataset

- 100,000 Candidate Profiles
- Career History
- Skills
- Education
- Behavioral Signals

---

## Output

The system produces:

outputs/ranked_candidates.csv

Columns:

- candidate_id
- rank
- score
- reasoning

---

## Future Improvements

- Cross-Encoder Re-ranking
- Learning-to-Rank Models
- LLM-Based Candidate Reasoning
- Recruiter Feedback Loops
- Real-Time Candidate Recommendations
