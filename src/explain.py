def build_reason(candidate):

    profile = candidate["profile"]

    title = profile["current_title"]

    exp = profile[
        "years_of_experience"
    ]

    response_rate = candidate[
        "redrob_signals"
    ][
        "recruiter_response_rate"
    ]

    notice = candidate[
        "redrob_signals"
    ][
        "notice_period_days"
    ]

    return (
        f"{title}; "
        f"{exp:.1f} yrs exp; "
        f"response={response_rate:.2f}; "
        f"notice={notice}d"
    )