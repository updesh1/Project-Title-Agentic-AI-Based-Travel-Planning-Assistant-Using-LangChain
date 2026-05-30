import json


def search_flight(source: str, destination: str):
    with open("data/flights.json", "r") as file:
        flights = json.load(file)

    matched_flights = [
        flight for flight in flights
        if flight["source"].lower() == source.lower()
        and flight["destination"].lower() == destination.lower()
    ]

    if not matched_flights:
        return None

    cheapest_flight = min(matched_flights, key=lambda x: x["price"])
    return cheapest_flight