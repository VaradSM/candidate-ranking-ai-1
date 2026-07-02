from src.preprocess import load_jd
from src.ranker import rank_candidates

jd = load_jd(
    "data/job_description.txt"
)

results = rank_candidates(
    jd,
    top_k=10
)

for row in results:
    print(row)