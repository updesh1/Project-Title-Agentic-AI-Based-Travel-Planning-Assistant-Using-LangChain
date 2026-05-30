import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

from tools.flight_tool import search_flight
from tools.hotel_tool import recommend_hotel
from tools.places_tool import discover_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget


load_dotenv()


def get_llm():
    return HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.3",
        task="text-generation",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        temperature=0.4,
        max_new_tokens=800
    )


def create_day_wise_itinerary(places, days):
    itinerary = {}

    for day in range(1, days + 1):
        start_index = (day - 1) % len(places)
        place = places[start_index]

        itinerary[f"Day {day}"] = {
            "morning": f"Visit {place['name']}",
            "afternoon": "Explore nearby local food and markets",
            "evening": "Relax and enjoy the city atmosphere"
        }

    return itinerary


def plan_trip(source, destination, days, budget, preference):
    flight = search_flight(source, destination)

    hotel_budget_per_night = int(budget * 0.35 / max(days - 1, 1))
    hotel = recommend_hotel(destination, hotel_budget_per_night)

    places = discover_places(destination, preference)

    if not places:
        places = discover_places(destination)

    weather = get_weather(destination, days)

    budget_breakdown = estimate_budget(flight, hotel, days)

    itinerary = create_day_wise_itinerary(places, days)

    llm = get_llm()

    prompt = f"""
You are an expert AI travel planner.

Create a clear and professional travel plan using this data:

Source: {source}
Destination: {destination}
Number of Days: {days}
User Budget: ₹{budget}
User Preference: {preference}

Selected Flight:
{flight}

Selected Hotel:
{hotel}

Places:
{places}

Weather:
{weather}

Budget Breakdown:
{budget_breakdown}

Day-wise Itinerary:
{itinerary}

Return the answer in this format:

1. Trip Summary
2. Selected Flight
3. Selected Hotel
4. Weather Forecast
5. Day-wise Itinerary
6. Budget Breakdown
7. Why these options were selected

Use simple English.
"""

    try:
        final_response = llm.invoke(prompt)
    except Exception as error:
        final_response = f"""
Trip Summary:
Trip from {source} to {destination} for {days} days.

Selected Flight:
{flight}

Selected Hotel:
{hotel}

Weather:
{weather}

Day-wise Itinerary:
{itinerary}

Budget Breakdown:
{budget_breakdown}

LLM Error:
{error}
"""

    return {
        "flight": flight,
        "hotel": hotel,
        "places": places,
        "weather": weather,
        "budget_breakdown": budget_breakdown,
        "itinerary": itinerary,
        "final_response": final_response
    }