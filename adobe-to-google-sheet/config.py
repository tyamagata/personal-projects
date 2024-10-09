from src.helpers import get_credentials

# Adobe API configuration
adobe_api_key = get_credentials("ADOBE_API_KEY")
adobe_client_secret = get_credentials("ADOBE_CLIENT_SECRET")
adobe_company_id = get_credentials("ADOBE_COMPANY_ID")

# Google Sheets configuration
google_sheets_config = {
    "customer1": {
        "spreadsheet_id": "SPREADSHEET_ID_FOR_CUSTOMER1",
        "date_tab": "Date",
        "conversions_tab": "Conversions"
    },
    "customer2": {
        "spreadsheet_id": "SPREADSHEET_ID_FOR_CUSTOMER2",
        "date_tab": "Date",
        "conversions_tab": "Conversions"
    }
    # Add additional customers as needed
}
