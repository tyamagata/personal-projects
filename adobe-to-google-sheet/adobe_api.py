import requests
import time
from src.config import adobe_api_key, adobe_client_secret, adobe_company_id
from src.helpers import get_credentials

class AdobeAPI:
    def __init__(self):
        self.api_key = adobe_api_key
        self.client_secret = adobe_client_secret
        self.company_id = adobe_company_id
        self.access_token = None
        self.token_expiry = 0

    def authenticate(self):
        """
        Authenticate with the Adobe API and get an access token.
        """
        token_url = "https://ims-na1.adobelogin.com/ims/token/v3"
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.client_secret,
            "scope": "openid,AdobeID,additional_info.projectedProductContext"
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = requests.post(token_url, headers=headers, data=payload)
        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data['access_token']
            self.token_expiry = time.time() + token_data['expires_in']
        else:
            raise Exception(f"Failed to authenticate: {response.content}")

    def get_token(self):
        """
        Get the current access token, refreshing it if it has expired.
        """
        if not self.access_token or time.time() > self.token_expiry:
            self.authenticate()
        return self.access_token

    def fetch_data(self, endpoint, payload):
        """
        Fetch data from the Adobe API.
        """
        if not self.access_token or time.time() > self.token_expiry:
            self.authenticate()

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

        response = requests.post(f"{endpoint}{self.company_id}/reports", 
                                 headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data: {response.content}")

    # Additional methods as needed for different types of API requests
