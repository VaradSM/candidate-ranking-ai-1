import os
import pickle
import numpy as np

from src.preprocess import (
    load_candidates,
    build_candidate_document
)

from src.embeddings import (
    get_embeddings_batch
)


def generate_candidate_embeddings():

    print("\nLoading candidates...")

    candidates = load_candidates(
        "data/candidates.jsonl"
    )

    print(
        f"Loaded {len(candidates)} candidates"
    )

    candidate_docs = []

    candidate_ids = []

    for candidate in candidates:

        candidate_docs.append(

            build_candidate_document(
                candidate
            )

        )

        candidate_ids.append(
            candidate["candidate_id"]
        )

    print(
        "\nGenerating embeddings..."
    )

    embeddings = get_embeddings_batch(
        candidate_docs
    )

    os.makedirs(
        "embeddings_store",
        exist_ok=True
    )

    np.save(

        "embeddings_store/candidate_embeddings.npy",

        embeddings

    )

    with open(

        "embeddings_store/candidate_ids.pkl",

        "wb"

    ) as f:

        pickle.dump(
            candidate_ids,
            f
        )

    print(
        "\nEmbeddings Saved Successfully"
    )

    print(
        f"Shape = {embeddings.shape}"
    )


if __name__ == "__main__":

    generate_candidate_embeddings()