from bs4 import BeautifulSoup
import requests


def scrape_ng_weather():
    """
    Scrape weather data from three states: ABeokuta, Bauchi and Benin City using beautiful
    """
    states_urls = {
        "Abeokuta":"https://www.timeanddate.com/weather/nigeria/abeokuta",
        "Bauchi":"https://www.timeanddate.com/weather/nigeria/bauchi",
        "Benin City":"https://www.timeanddate.com/weather/nigeria/benin-city"
    }
    weather_ng_data = {}

    try:
        for city, states_urls in states_urls.items():
            response  = requests.get(states_urls)
            response.raise_for_status() # ensure request was successfull

            soup = BeautifulSoup(response.content, "lxml")
            
            
            # Extract relevant weather details
            temperature = soup.find("div", class_="h2").text.strip() if soup.find("div", class_="h2") else "N/A"
            humidity = soup.find("th", text="Humidity").find_next_sibling("td").text.strip() if soup.find("th", text="Humidity") else "N/A"
            pressure = soup.find("th", text="Pressure").find_next_sibling("td").text.strip() if soup.find("th", text="Pressure") else "N/A"
            dew_point = soup.find("th", text="Dew Point").find_next_sibling("td").text.strip() if soup.find("th", text="Dew Point") else "N/A"
            visibility = soup.find("th", text="Visibility").find_next_sibling("td").text.strip() if soup.find("th", text="Visibility") else "N/A"
            # wind = soup.find("th", text="Wind").find_next_sibling("td").text.strip() if soup.find("td", text="Wind") else "N/A"
            
            # Store the extracted data
            weather_ng_data[city] = {
                "Temperature": temperature,
                "Humidity": humidity,
                "Pressure": pressure,
                "Dew Point": dew_point,
                "Visibility": visibility,
                # "Wind": wind
            }

        
        return weather_ng_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather states data: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

print(scrape_ng_weather())