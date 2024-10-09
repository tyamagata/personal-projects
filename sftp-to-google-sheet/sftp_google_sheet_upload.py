import paramiko
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import os
import tempfile
from config import google_service_account_credentials, CUSTOMERS

# Initialize Google Sheets client
credentials = ServiceAccountCredentials.from_json_keyfile_dict(google_service_account_credentials)
gc = gspread.authorize(credentials)

def download_sftp_file(sftp_config):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        local_filepath = temp_file.name
        transport = paramiko.Transport((sftp_config['host'], 22))
        transport.connect(username=sftp_config['username'], password=sftp_config['password'])
        sftp = paramiko.SFTPClient.from_transport(transport)
        
        directory, filename = os.path.split(sftp_config['file_path'])
        if directory:  # Check if the directory path is not empty
            sftp.chdir(directory)
        
        sftp.get(filename, local_filepath)
        print(f"Downloaded {filename} to {local_filepath}")
        
        sftp.close()
        transport.close()
        
    return local_filepath

def upload_to_google_sheet(customer_config, filepath):
    sheet = gc.open_by_key(customer_config['google_sheets']['sheet_id']).worksheet(customer_config['google_sheets']['tab_name'])
    sheet.clear()  # Clear existing data in the sheet
    with open(filepath, 'r') as file_obj:
        csv_reader = csv.reader(file_obj)
        rows = list(csv_reader)
        if rows:  # Ensure there is data to upload
            sheet.update('A1', rows)  # Update sheet starting at cell A1
            print(f"Uploaded data to Google Sheet: {customer_config['google_sheets']['sheet_id']}")
    
    os.remove(filepath)  # Clean up the temporary file

def main():
    for customer in CUSTOMERS:
        print(f"Processing {customer['customer_name']}...")
        local_filepath = download_sftp_file(customer['sftp'])
        upload_to_google_sheet(customer, local_filepath)

if __name__ == "__main__":
    main()
