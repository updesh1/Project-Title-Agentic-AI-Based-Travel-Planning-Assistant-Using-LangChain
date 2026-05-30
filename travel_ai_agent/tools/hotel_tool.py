import json


def recommend_hotel(city: str, max_price: int = None):
    with open("data/hotels.json", "r") as file:
        hotels = json.load(file)

    matched_hotels = [
        hotel for hotel in hotels
        if hotel["city"].lower() == city.lower()
    ]

    if max_price:
        matched_hotels = [
            hotel for hotel in matched_hotels
            if hotel["price_per_night"] <= max_price
        ]

    if not matched_hotels:
        return None

    best_hotel = max(matched_hotels, key=lambda x: x["rating"])
    return best_hotel