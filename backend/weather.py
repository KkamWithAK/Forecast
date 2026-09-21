import os
import requests
from dotenv import load_dotenv
from models import WeatherData

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", default="")
POSTCODE = os.getenv("POSTCODE", default="")


async def  get_weather():
    print("POSTCODE",POSTCODE)
    url = "https://api.weatherapi.com/v1/forecast.json"
    payload  = {
        "key": WEATHER_API_KEY,
        "q": POSTCODE,
        "days":1,
        "aqi":"no",
        "alerts":"no",

    }
    headers = {
        "accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url=url,
        params=payload,
        headers=headers
    )
    response.raise_for_status()
    day = response.json()["forecast"]["forecastday"][0]["day"]
    city = response.json()["location"]["name"]
    average_temp = day["avgtemp_c"]
    rain = day["daily_will_it_rain"]
    condition = day["condition"]["text"]
    icon =day["condition"]["icon"]
    weatherData = WeatherData(city= city, average_temp =average_temp, rain =rain,condition = condition, icon = icon)
    return weatherData