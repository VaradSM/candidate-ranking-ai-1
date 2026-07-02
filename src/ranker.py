import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from src.embeddings import get_embedding

from src.scoring import final_score

from src.explain import build_reason


def rank_candidates(
        jd_text,
        candidates,
        embeddings,
        top_k=500
):

    jd_embedding = get_embedding(
        jd_text
    ).reshape(1, -1)

    similarities = cosine_similarity(
        jd_embedding,
        embeddings
    )[0]

    scored = []

    for idx, candidate in enumerate(
            candidates
    ):

        semantic = float(
            similarities[idx]
        )

        score = final_score(
            semantic,
            candidate
        )

        scored.append({

            "candidate_id":
            candidate["candidate_id"],

            "score":
            score,

            "reasoning":
            build_reason(candidate)

        })

    scored = sorted(

        scored,

        key=lambda x:
        x["score"],

        reverse=True

    )

    return scored[:top_k]