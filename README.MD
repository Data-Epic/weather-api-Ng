# Weather Scraper API
## 📌 Project Overview
The Weather Scraper API is a FastAPI-based web service that scrapes weather data for Nigerian states (**Abeokuta, Bauchi and Benin City**). It processes the data and then writes it to a Google sheet using **gspread**. The API also provide a GET endpoint that retrieves the latest stored weather data.

## ⚡Features
1. FastAPI Endpoint: Exposes a GET endpoint (`/weather`) to fetch the latest weather data.
2. Extracts weather data using `BeautifulSoup`.
3. Google Sheets Integration: Writes scraped data to a Google Sheet using `gspread`.
4. Dependency Management: Uses `poetry` for managing dependencies.
5. Testing: Includes test cases with `pytest`.
6. Uses virtual environment for an isolated python environment.

## 🛠️ Installation & Setup
### 1. Clone the Repository
```
git clone https://github.com/DarkKnight845/Weather-API-Ng
```
### 2. Set Up Virtual Environment
```
python -m venv venv
source venv/bin/activate # For Linux/macOS
venv\Scripts\activate # For Windows
```
### 3. Install Dependencies with Poetry
```
poetry install package
```
### 4. Set Up Google Sheets Credentials
1. Create a Service account on Google Cloud Console.
2. Download the JSON credentials file.
3. Save it as `service_account` inside the project directory.
4. Share the Google Sheet with the service account email.

## 🚀 Running the API
### Start the FastAPI Server
`poetry uvicorn main:app --reload`
### Test the API via Swagger UI
`http://127.0.0.1:8000/weather/update`

## 🧪 Running Tests
To run tests using `pytest`:
```
pytest
```

## 🧑‍🤝‍🧑 Dependencies
1. FastAPI 
2. BeautifulSoup
3. Requests 
4. Gspread 
5. Pytest


