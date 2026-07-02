import json


def load_candidates(filepath):

    candidates = []

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            candidates.append(
                json.loads(line)
            )

    return candidates


def load_jd(filepath):

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


def extract_skill_names(candidate):

    skills = candidate.get(
        "skills",
        []
    )

    return [

        skill["name"]

        for skill in skills

    ]


def build_career_text(candidate):

    career_entries = candidate.get(
        "career_history",
        []
    )

    career_text = []

    for role in career_entries:

        company = role.get(
            "company",
            ""
        )

        title = role.get(
            "title",
            ""
        )

        description = role.get(
            "description",
            ""
        )

        industry = role.get(
            "industry",
            ""
        )

        career_text.append(

            f"""
            Title: {title}
            Company: {company}
            Industry: {industry}
            Description: {description}
            """

        )

    return "\n".join(
        career_text
    )


def build_education_text(candidate):

    education = candidate.get(
        "education",
        []
    )

    rows = []

    for edu in education:

        rows.append(

            f"""
            Institution: {edu.get('institution', '')}
            Degree: {edu.get('degree', '')}
            Field: {edu.get('field_of_study', '')}
            Tier: {edu.get('tier', 'unknown')}
            """

        )

    return "\n".join(rows)


def build_skill_text(candidate):

    skills = candidate.get(
        "skills",
        []
    )

    rows = []

    for skill in skills:

        rows.append(

            f"""
            Skill: {skill.get('name', '')}
            Proficiency: {skill.get('proficiency', '')}
            Endorsements: {skill.get('endorsements', 0)}
            Duration Months: {skill.get('duration_months', 0)}
            """

        )

    return "\n".join(rows)


def build_candidate_document(candidate):

    profile = candidate["profile"]

    headline = profile.get(
        "headline",
        ""
    )

    summary = profile.get(
        "summary",
        ""
    )

    current_title = profile.get(
        "current_title",
        ""
    )

    current_company = profile.get(
        "current_company",
        ""
    )

    years_exp = profile.get(
        "years_of_experience",
        0
    )

    industry = profile.get(
        "current_industry",
        ""
    )

    skills_text = build_skill_text(
        candidate
    )

    career_text = build_career_text(
        candidate
    )

    education_text = build_education_text(
        candidate
    )

    document = f"""

    HEADLINE
    {headline}

    SUMMARY
    {summary}

    CURRENT ROLE
    {current_title}

    CURRENT COMPANY
    {current_company}

    YEARS OF EXPERIENCE
    {years_exp}

    CURRENT INDUSTRY
    {industry}

    CAREER HISTORY
    {career_text}

    EDUCATION
    {education_text}

    SKILLS
    {skills_text}

    """

    return document