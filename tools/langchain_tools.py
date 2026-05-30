import json
from langchain_core.tools import tool

from tools.flight_tool import search_flight
from tools.hotel_tool import recommend_hotel
from tools.places_tool import discover_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget


def parse_json_input(query: str):
    try:
        return json.loads(query)
    except Exception:
        return {}


@tool
def flight_search_tool(query: str) -> str:
    """
    Search cheapest flight.
    Input JSON format:
    {"source": "Delhi", "destination": "Goa"}
    """
    data = parse_json_input(query)
    result = search_flight(
        data.get("source", ""),
        data.get("destination", "")
    )
    return json.dumps(result, indent=2)


@tool
def hotel_recommendation_tool(query: str) -> str:
    """
    Recommend best hotel.
    Input JSON format:
    {"city": "Goa", "max_price": 4000}
    """
    data = parse_json_input(query)
    result = recommend_hotel(
        data.get("city", ""),
        data.get("max_price")
    )
    return json.dumps(result, indent=2)


@tool
def places_discovery_tool(query: str) -> str:
    """
    Discover tourist places.
    Input JSON format:
    {"city": "Goa", "preference": "Beach"}
    """
    data = parse_json_input(query)
    result = discover_places(
        data.get("city", ""),
        data.get("preference", "")
    )
    return json.dumps(result, indent=2)


@tool
def weather_lookup_tool(query: str) -> str:
    """
    Get weather forecast.
    Input JSON format:
    {"city": "Goa", "days": 3}
    """
    data = parse_json_input(query)
    result = get_weather(
        data.get("city", ""),
        int(data.get("days", 3))
    )
    return json.dumps(result, indent=2)


@tool
def budget_estimation_tool(query: str) -> str:
    """
    Estimate travel budget.
    Input JSON format:
    {
      "flight": {"price": 4800},
      "hotel": {"price_per_night": 3200},
      "days": 3
    }
    """
    data = parse_json_input(query)

    result = estimate_budget(
        data.get("flight"),
        data.get("hotel"),
        int(data.get("days", 3))
    )

    return json.dumps(result, indent=2)