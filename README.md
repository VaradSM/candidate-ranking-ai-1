# AI Candidate Ranking System

## Overview
An AI-powered candidate ranking engine that ranks candidates against a job description using:

- Semantic similarity (Sentence Transformers)
- Career relevance scoring
- Behavioral signal scoring
- Location preference scoring

## Project Structure

src/

preprocess.py

embeddings.py

generate_embeddings.py

feature_engineering.py

career_score.py

behavior_score.py

location_score.py

scoring.py

ranker.py

## Methodology

Final Score =
0.60 × Semantic Similarity +
0.20 × Career Score +
0.10 × Behavior Score +
0.10 × Location Score

## Installation

pip install -r requirements.txt

## Run

python test.py

## Output

outputs/ranked_candidates.csv
