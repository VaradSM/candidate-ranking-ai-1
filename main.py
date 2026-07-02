import pandas as pd

from src.preprocess import (
    load_candidates
)

from src.ranker import (
    rank_candidates
)

from src.config import (
    CANDIDATES_FILE,
    JD_FILE,
    EMBEDDINGS_FILE
)

import numpy as np


def load_jd():

    with open(
        JD_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


def main():

    print(
        "Loading candidates..."
    )

    candidates = load_candidates(
        CANDIDATES_FILE
    )

    print(
        f"{len(candidates)} loaded"
    )

    print(
        "Loading embeddings..."
    )

    embeddings = np.load(
        EMBEDDINGS_FILE
    )

    jd = load_jd()

    print(
        "Ranking candidates..."
    )

    ranked = rank_candidates(
        jd,
        candidates,
        embeddings,
        top_k=100
    )

    rows = []

    for rank, item in enumerate(
            ranked,
            start=1
    ):

        rows.append({

            "candidate_id":
            item["candidate_id"],

            "rank":
            rank,

            "score":
            round(
                item["score"],
                4
            ),

            "reasoning":
            item["reasoning"]
        })

    df = pd.DataFrame(rows)

    output_file = (
        "outputs/"
        "ranked_candidates.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved: {output_file}"
    )

    print(
        df.head()
    )


if __name__ == "__main__":
    main()