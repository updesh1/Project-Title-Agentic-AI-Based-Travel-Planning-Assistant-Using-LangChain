import json


def discover_places(city: str, preference: str = None):
    with open("data/places.json", "r") as file:
        places = json.load(file)

    matched_places = [
        place for place in places
        if place["city"].lower() == city.lower()
    ]

    if preference:
        preferred_places = [
            place for place in matched_places
            if preference.lower() in place["type"].lower()
        ]

        if preferred_places:
            matched_places = preferred_places

    sorted_places = sorted(
        matched_places,
        key=lambda x: x["rating"],
        reverse=True
    )

    return sorted_places[:6]