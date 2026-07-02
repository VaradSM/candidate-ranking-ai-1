INDIAN_HUBS = [

    "pune",
    "noida",
    "delhi",
    "new delhi",
    "gurgaon",
    "gurugram",
    "mumbai",
    "hyderabad",
    "bangalore",
    "bengaluru"
]


def location_score(candidate):

    score = 0

    profile = candidate["profile"]

    location = profile["location"].lower()

    country = profile["country"].lower()

    if country == "india":
        score += 50

    if any(
        city in location
        for city in INDIAN_HUBS
    ):
        score += 50

    return min(score, 100)