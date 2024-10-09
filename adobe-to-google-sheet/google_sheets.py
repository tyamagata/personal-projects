from googleapiclient.discovery import build
from google.oauth2 import service_account
from src.config import google_sheets_config
import pandas as pd

class GoogleSheets:
    def __init__(self, customer_name):
        self.spreadsheet_id, self.tabs = self.get_config_for_customer(customer_name)
        self.creds = self.get_credentials()
        self.service = build('sheets', 'v4', credentials=self.creds)

    def get_credentials(self):
        # Replace 'path/to/your/service/account/key.json' with the path to your Google service account key file
        creds = service_account.Credentials.from_service_account_file(
            'path/to/your/service/account/key.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        return creds

    def get_config_for_customer(self, customer_name):
        return google_sheets_config[customer_name]['spreadsheet_id'], google_sheets_config[customer_name]['tabs']

    def clear_sheet(self, sheet_name):
        range = f"{sheet_name}!A:Z"  # Adjust range as needed
        self.service.spreadsheets().values().clear(
            spreadsheetId=self.spreadsheet_id, range=range, body={}).execute()

    def update_sheet(self, data, sheet_name):
        # Converts data to a format suitable for Google Sheets
        values = [list(data.columns)] + data.values.tolist()
        body = {'values': values}
        self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, range=f"{sheet_name}!A1", 
            valueInputOption='RAW', body=body).execute()

    def read_sheet(self, sheet_name, range):
        # Reads and returns data from a specific sheet and range
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, range=f"{sheet_name}!{range}").execute()
        return pd.DataFrame(result.get('values', []))
