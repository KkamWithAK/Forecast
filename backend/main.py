import requests
from dotenv import load_dotenv
import fastapi
from fastapi import FastAPI
import weather
from models import WeatherData

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/information")
async def information():
    data = await weather.get_weather()
    return data
    #return {"message": "Returns a Json containing: an itinerary, path to calender tts file, forcast info, forcast tts"}