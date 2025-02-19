from fastapi import FastAPI
from scrapper.google_sheet import write_to_sheet
from  scrapper.scrapper import scrape_ng_weather


app = FastAPI()

@app.get("/")
def home():
    return "Weather Scrapper API is running"

@app.get("/weather/update")
def update_weather():
    """
    Fetch weather data
    Write into google sheet
    Return strored data
    """
    
    weather_data = scrape_ng_weather()

    if not weather_data:
        return {"Failed to retrieve weather data"}
    
    result = write_to_sheet(weather_data)
    return {"message": result, "data": weather_data}