from src.adobe_api import AdobeAPI
from src.google_sheets import GoogleSheets
from src.helpers import process_adobe_data, format_data_for_sheets
from src.config import google_sheets_config  # Assuming google_sheets_config is in config.py

def main(customer_name):
    # Initialize Adobe API
    adobe_api = AdobeAPI()

    # Example: Define the payload for Adobe API request
    # Replace this with your actual payload
    payload = {
        # Your payload structure goes here
    }

    # Fetch data from Adobe API
    adobe_response = adobe_api.fetch_data(endpoint="YOUR_ENDPOINT", payload=payload)

    # Process Adobe API data
    processed_data = process_adobe_data(adobe_response)

    # Initialize Google Sheets with customer-specific configuration
    google_sheets = GoogleSheets(customer_name)

    # Clear existing data in the "Date" tab
    google_sheets.clear_sheet(google_sheets.tabs['date'])

    # Clear existing data in the "Conversions" tab
    google_sheets.clear_sheet(google_sheets.tabs['conversions'])

    # Format data for Google Sheets and update the "Date" tab
    formatted_date_data = format_data_for_sheets(processed_data['date'])
    google_sheets.update_sheet(formatted_date_data, google_sheets.tabs['date'])

    # Format data for Google Sheets and update the "Conversions" tab
    formatted_conversions_data = format_data_for_sheets(processed_data['conversions'])
    google_sheets.update_sheet(formatted_conversions_data, google_sheets.tabs['conversions'])

    print("Data updated successfully in Google Sheets.")

if __name__ == "__main__":
    customer_name = "customer1"  # Replace with dynamic customer name as needed
    main(customer_name)
