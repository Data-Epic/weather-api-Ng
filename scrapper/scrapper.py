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

            # Loacate weather states tbale 
            table = soup.find("table", class_="zebra tb-wt tc sep")

            # Extract the headers 
            headers = [th.get_text(strip=True) for th in table.find_all("th")]

            # Exxtract rows
            rows = []
            for tr in table.find_all('tr')[1:]:
                columns = [td.get_text(strip=True) for td in tr.find_all("td")]
            if columns:
                row_data = dict(zip(headers, columns))
                rows.append(row_data)
            
            weather_ng_data[city] = rows
        
        return weather_ng_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather states data: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None