"""
Global Configuration
"""

# ====================================
# Embedding Model
# ====================================

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# ====================================
# Retrieval
# ====================================

TOP_K_RETRIEVAL = 2000

# ====================================
# Final Submission
# ====================================

TOP_K_SUBMISSION = 100

# ====================================
# Scoring Weights
# ====================================

WEIGHTS = {

    "semantic_similarity": 0.55,

    "skill_score": 0.10,

    "experience_score": 0.10,

    "behavior_score": 0.15,

    "profile_quality_score": 0.05,

    "industry_score": 0.05

}

CANDIDATES_FILE = "data/candidates.jsonl"

JD_FILE = "data/job_description.txt"

EMBEDDINGS_FILE = (
    "embeddings_store/"
    "candidate_embeddings.npy"
)