from pydantic import BaseModel

class WeatherData(BaseModel):
    city: str
    average_temp: float
    rain: int
    condition: str
    icon: str
