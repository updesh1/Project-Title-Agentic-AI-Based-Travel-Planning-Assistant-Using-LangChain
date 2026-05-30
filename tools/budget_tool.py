def estimate_budget(flight, hotel, days: int, food_per_day: int = 800, local_travel_per_day: int = 500):
    flight_cost = flight["price"] if flight else 0
    hotel_cost = hotel["price_per_night"] * max(days - 1, 1) if hotel else 0
    food_cost = food_per_day * days
    local_travel_cost = local_travel_per_day * days

    total = flight_cost + hotel_cost + food_cost + local_travel_cost

    return {
        "flight_cost": flight_cost,
        "hotel_cost": hotel_cost,
        "food_cost": food_cost,
        "local_travel_cost": local_travel_cost,
        "total_cost": total
    }