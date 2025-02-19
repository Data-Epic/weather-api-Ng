import pytest
from scrapper.scrapper import scrape_ng_weather

def test_sccrape_weather():
    """
    Test if the scrape weather function returns valid data 
    """
    weather_data = scrape_ng_weather()

    # ensuring the response is a dictionary
    assert isinstance(weather_data, dict)

    # checking if the cities/states exist in the response
    cities = {"Abeokuta", "Bauchi", "Benin City"}
    assert cities.issubset(weather_data.keys())

    # checking if each city's data contains a list
    for city, data in weather_data.items():
        assert isinstance(data, list)
        if data: # checking if the first entry has data
            assert isinstance(data[0], dict)