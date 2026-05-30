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
    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    if not token:
        raise ValueError("HUGGINGFACEHUB_API_TOKEN is missing in .env file")

    return HuggingFaceEndpoint(
        repo_id="google/flan-t5-large",
        task="text2text-generation",
        huggingfacehub_api_token=token,
        temperature=0.3,
        max_new_tokens=700
    )


def create_day_wise_itinerary(places, days):
    itinerary = {}

    if not places:
        return {"message": "No places found"}

    for day in range(1, days + 1):
        place = places[(day - 1) % len(places)]

        itinerary[f"Day {day}"] = {
            "Morning": f"Visit {place['name']}",
            "Afternoon": "Explore local food and nearby markets",
            "Evening": "Relax at hotel or nearby area"
        }

    return itinerary


def generate_fallback_plan(
    source,
    destination,
    days,
    budget,
    preference,
    flight,
    hotel,
    places,
    weather,
    budget_breakdown,
    itinerary
):
    if flight:
        flight_text = f"""
Airline: {flight['airline']}  
Price: ₹{flight['price']}  
Departure: {flight['departure']}  
Arrival: {flight['arrival']}  
Duration: {flight['duration']}
"""
    else:
        flight_text = "No direct flight found in the available dataset."

    if hotel:
        hotel_text = f"""
Hotel Name: {hotel['name']}  
Rating: {hotel['rating']} ⭐  
Price per Night: ₹{hotel['price_per_night']}  
Category: {hotel['type']}
"""
    else:
        hotel_text = "No suitable hotel found in the available dataset."

    weather_text = ""

    if weather:
        for day in weather:
            weather_text += f"""
Day {day['day']} - {day['date']}  
Max Temperature: {day['max_temp']}°C  
Min Temperature: {day['min_temp']}°C  
Weather Code: {day['weather_code']}  

"""
    else:
        weather_text = "Weather data is not available."

    itinerary_text = ""

    if itinerary:
        for day, details in itinerary.items():
            itinerary_text += f"""
## {day}

Morning: {details['Morning']}  
Afternoon: {details['Afternoon']}  
Evening: {details['Evening']}  

"""
    else:
        itinerary_text = "No itinerary could be created."

    return f"""
# Trip Summary

From: {source}  
To: {destination}  
Duration: {days} Days  
Budget: ₹{budget}  
Travel Preference: {preference}  

---

# Selected Flight

{flight_text}

---

# Recommended Hotel

{hotel_text}

---

# Weather Forecast

{weather_text}

---

# Day Wise Itinerary

{itinerary_text}

---

# Budget Breakdown

Flight Cost: ₹{budget_breakdown['flight_cost']}  
Hotel Cost: ₹{budget_breakdown['hotel_cost']}  
Food Cost: ₹{budget_breakdown['food_cost']}  
Local Travel Cost: ₹{budget_breakdown['local_travel_cost']}  

## Total Estimated Cost: ₹{budget_breakdown['total_cost']}

---

# Why These Options Were Selected

The flight was selected based on the cheapest available option.  
The hotel was selected based on rating and budget.  
The places were selected based on your travel preference and ratings.  
The budget was calculated using flight, hotel, food, and local travel cost.
"""


def plan_trip_with_agent(source, destination, days, budget, preference):
    try:
        flight = search_flight(source, destination)

        hotel_budget_per_night = int(budget * 0.35 / max(days - 1, 1))
        hotel = recommend_hotel(destination, hotel_budget_per_night)

        if hotel is None:
            hotel = recommend_hotel(destination)

        places = discover_places(destination, preference)

        if not places:
            places = discover_places(destination)

        weather = get_weather(destination, days)

        budget_breakdown = estimate_budget(flight, hotel, days)

        itinerary = create_day_wise_itinerary(places, days)

        fallback_plan = generate_fallback_plan(
            source=source,
            destination=destination,
            days=days,
            budget=budget,
            preference=preference,
            flight=flight,
            hotel=hotel,
            places=places,
            weather=weather,
            budget_breakdown=budget_breakdown,
            itinerary=itinerary
        )

        try:
            llm = get_llm()

            prompt = f"""
Improve this travel plan in simple professional English:

{fallback_plan}
"""

            response = llm.invoke(prompt)

            if response:
                return response

            return fallback_plan

        except Exception:
            return fallback_plan

    except Exception as error:
        return f"""
# Critical Error

{repr(error)}
"""