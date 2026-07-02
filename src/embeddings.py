from sentence_transformers import SentenceTransformer

from src.config import (
    EMBEDDING_MODEL
)

print(
    f"Loading embedding model: {EMBEDDING_MODEL}"
)

model = SentenceTransformer(
    EMBEDDING_MODEL
)


def get_embedding(text):

    embedding = model.encode(

        text,

        normalize_embeddings=True,

        convert_to_numpy=True

    )

    return embedding


def get_embeddings_batch(texts):

    embeddings = model.encode(

        texts,

        batch_size=64,

        show_progress_bar=True,

        normalize_embeddings=True,

        convert_to_numpy=True

    )

    return embeddings