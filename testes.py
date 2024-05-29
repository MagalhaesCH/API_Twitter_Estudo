import unittest
from app.auth import get_bearer_token
from app.data_collection import search_tweets

class TestTwitterAPI(unittest.TestCase):
    def test_get_bearer_token(self):
        api_key = "fake_api_key"
        api_secret_key = "fake_api_secret_key"
        token = get_bearer_token(api_key, api_secret_key)
        self.assertIsNotNone(token)

    def test_search_tweets(self):
        bearer_token = "fake_bearer_token"
        tweets = search_tweets("#example", bearer_token)
        self.assertGreater(len(tweets['statuses']), 0)

if __name__ == "__main__":
    unittest.main()
