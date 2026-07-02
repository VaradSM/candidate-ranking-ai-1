from src.career_score import career_score
from src.behavior_score import behavior_score
from src.location_score import location_score


def final_score(
        semantic_score,
        candidate
):

    career = (
        career_score(candidate)
        / 100
    )

    behavior = (
        behavior_score(candidate)
        / 100
    )

    location = (
        location_score(candidate)
        / 100
    )

    score = (

        0.50 * semantic_score +

        0.30 * career +

        0.15 * behavior +

        0.05 * location
    )

    return score