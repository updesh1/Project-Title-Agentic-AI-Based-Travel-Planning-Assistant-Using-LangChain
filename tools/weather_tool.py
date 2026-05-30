import requests


CITY_COORDINATES = {
    "Goa": {"latitude": 15.2993, "longitude": 74.1240},
    "Delhi": {"latitude": 28.6139, "longitude": 77.2090},
    "Mumbai": {"latitude": 19.0760, "longitude": 72.8777},
    "Lucknow": {"latitude": 26.8467, "longitude": 80.9462},
    "Jaipur": {"latitude": 26.9124, "longitude": 75.7873},
    "Agra": {"latitude": 27.1767, "longitude": 78.0081},
    "Varanasi": {"latitude": 25.3176, "longitude": 82.9739},
    "Udaipur": {"latitude": 24.5854, "longitude": 73.7125},
    "Manali": {"latitude": 32.2432, "longitude": 77.1892},
    "Shimla": {"latitude": 31.1048, "longitude": 77.1734},
    "Kerala": {"latitude": 10.8505, "longitude": 76.2711},
    "Darjeeling": {"latitude": 27.0410, "longitude": 88.2663}
}


def get_weather(city: str, days: int):
    city_data = CITY_COORDINATES.get(city.title())

    if not city_data:
        return []

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": city_data["latitude"],
        "longitude": city_data["longitude"],
        "daily": "temperature_2m_max,temperature_2m_min,weather_code",
        "timezone": "auto",
        "forecast_days": days
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        weather_list = []

        for i in range(days):
            weather_list.append({
                "day": i + 1,
                "date": data["daily"]["time"][i],
                "max_temp": data["daily"]["temperature_2m_max"][i],
                "min_temp": data["daily"]["temperature_2m_min"][i],
                "weather_code": data["daily"]["weather_code"][i]
            })

        return weather_list

    except requests.RequestException:
        return []