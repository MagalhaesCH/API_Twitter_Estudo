import requests
import os
from requests.auth import HTTPBasicAuth

def get_bearer_token(api_key, api_secret_key):
    url = "https://api.twitter.com/oauth2/token"
    auth = HTTPBasicAuth(api_key, api_secret_key)
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    data = {"grant_type": "client_credentials"}
    
    response = requests.post(url, headers=headers, data=data, auth=auth)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Cannot get a Bearer token (HTTP {response.status_code}): {response.text}")

if __name__ == "__main__":
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret_key = os.getenv("TWITTER_API_SECRET_KEY")
    token = get_bearer_token(api_key, api_secret_key)
    print(f"Bearer Token: {token}")
