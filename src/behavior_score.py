from datetime import datetime


def normalize(value, max_value):

    return min(
        value / max_value,
        1.0
    )


def behavior_score(candidate):

    signals = candidate["redrob_signals"]

    score = 0

    score += (
        signals["recruiter_response_rate"]
        * 30
    )

    score += (
        signals["interview_completion_rate"]
        * 20
    )

    score += normalize(
        signals["saved_by_recruiters_30d"],
        20
    ) * 10

    score += normalize(
        signals["search_appearance_30d"],
        500
    ) * 10

    score += normalize(
        signals["profile_views_received_30d"],
        300
    ) * 10

    if signals["open_to_work_flag"]:
        score += 10

    if signals["verified_email"]:
        score += 5

    if signals["verified_phone"]:
        score += 5

    if signals["linkedin_connected"]:
        score += 5

    notice = signals["notice_period_days"]

    if notice <= 30:
        score += 10

    elif notice > 60:
        score -= 5

    return max(
        min(score, 100),
        0
    )