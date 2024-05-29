import requests
import os

def search_tweets(query, bearer_token, count=100):
    url = f"https://api.twitter.com/1.1/search/tweets.json?q={query}&count={count}"
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching tweets (HTTP {response.status_code}): {response.text}")

if __name__ == "__main__":
    query = "#example"
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    tweets = search_tweets(query, bearer_token)
    print(tweets)
