from datetime import datetime


AI_SKILLS = {

    "python",
    "llm",
    "rag",
    "transformers",
    "embeddings",
    "vector search",
    "faiss",
    "milvus",
    "pinecone",
    "qdrant",
    "langchain",
    "lora",
    "fine-tuning llms",
    "machine learning",
    "deep learning",
    "nlp"

}


def skill_score(candidate):

    skills = {

        x["name"].lower()
        for x in candidate["skills"]

    }

    matches = skills & AI_SKILLS

    return len(matches) / len(AI_SKILLS)


def experience_score(candidate):

    years = candidate["profile"][
        "years_of_experience"
    ]

    if 5 <= years <= 9:
        return 1.0

    if 3 <= years < 5:
        return 0.8

    if years > 9:
        return 0.7

    return 0.4


def behavior_score(candidate):

    signals = candidate[
        "redrob_signals"
    ]

    completeness = (
        signals[
            "profile_completeness_score"
        ] / 100
    )

    response_rate = signals[
        "recruiter_response_rate"
    ]

    github = max(
        signals[
            "github_activity_score"
        ],
        0
    ) / 100

    interview = signals[
        "interview_completion_rate"
    ]

    return (

        0.35 * completeness +
        0.25 * response_rate +
        0.20 * github +
        0.20 * interview

    )


def stability_score(candidate):

    history = candidate[
        "career_history"
    ]

    avg_months = (

        sum(
            x["duration_months"]
            for x in history
        )

        /

        len(history)

    )

    return min(
        avg_months / 36,
        1
    )