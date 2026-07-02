AI_TITLES = [
    "ai engineer",
    "ml engineer",
    "machine learning engineer",
    "data scientist",
    "applied ml engineer",
    "search engineer",
    "recommendation engineer",
    "nlp engineer",
    "llm engineer",
    "ai architect"
]

SEARCH_TITLES = [
    "search engineer",
    "recommendation engineer",
    "retrieval engineer"
]

RESEARCH_TITLES = [
    "research engineer",
    "research scientist",
    "applied scientist"
]

HIGH_VALUE_KEYWORDS = {

    "retrieval": 15,
    "ranking": 15,
    "recommendation": 15,
    "search": 10,

    "embeddings": 10,
    "vector": 10,
    "semantic search": 15,

    "faiss": 15,
    "milvus": 15,
    "pinecone": 15,
    "qdrant": 15,
    "weaviate": 15,

    "ndcg": 15,
    "mrr": 15,
    "map": 15,

    "a/b testing": 10,
    "ab testing": 10,

    "llm": 5,
    "fine-tuning": 5,
    "lora": 5
}

CONSULTING_COMPANIES = [
    "tcs",
    "infosys",
    "wipro",
    "accenture",
    "cognizant",
    "capgemini",
    "mindtree",
    "tech mahindra",
    "hcl"
]


def career_score(candidate):

    score = 0

    title = candidate["profile"]["current_title"].lower()

    if any(x in title for x in AI_TITLES):
        score += 35

    if any(x in title for x in SEARCH_TITLES):
        score += 25

    if any(x in title for x in RESEARCH_TITLES):
        score -= 15

    full_text = ""

    for role in candidate["career_history"]:

        full_text += (
            role["title"] +
            " " +
            role["description"] +
            " "
        ).lower()

    for keyword, weight in HIGH_VALUE_KEYWORDS.items():

        if keyword in full_text:
            score += weight

    career = candidate["career_history"]

    all_consulting = True

    for role in career:

        company = role["company"].lower()

        if not any(
            x in company
            for x in CONSULTING_COMPANIES
        ):
            all_consulting = False
            break

    if all_consulting:
        score -= 15

    return max(
        min(score, 100),
        0
    )