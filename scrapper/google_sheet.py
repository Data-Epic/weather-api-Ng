import gspread
from scrapper import scrape_ng_weather
from google.oauth2.service_account import Credentials

def write_to_sheet(weather_data):
    """
    writes data to google sheet
    """
    try:
        print("Authenticating Google Sheets API....")
        # google sheets credentials
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        SERVICE_ACCOUNT_FILE = "service_account.json"
        # authenticate and initialize google sheets client
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        client = gspread.authorize(creds)

        print(" Connecting to Google Sheet")

        weather_ng_sheet_id = "1W3dLAmITlXTZXzFfatxBCm7nE3bdDBMoi2yg1oily08"
        sheet = client.open_by_key(weather_ng_sheet_id)
        worksheet = sheet.sheet1
        worksheet.clear()

        print("Succesfully connected to Google Sheets")

        for city, data in weather_data.items():
            print(f"Writing data for {city}...")

            if not data:
                print(f"No data for {city}")
                continue

            headers = ["City", "Temperature", "Humidity", "Pressure", "Dew Point", "Visibility"]
            worksheet.append_row([city])
            worksheet.append_row(headers)

            row = [data["Temperature"], data["Humidity"], data["Pressure"], 
                   data["Dew Point"], data["Visibility"]]
            worksheet.append_row(row)

            print("Succesfully wrote all weather data to Google Sheeets")


    except gspread.exceptions.SpreadsheetNotFound:
        print("Error: Spreadsheet not found")
    except gspread.exceptions.APIError as api_error:
        print(f"Google Sheets API error: {api_error}")
    except Exception as e:
        print(f"Unexpected error: {e}")


print(write_to_sheet(scrape_ng_weather()))