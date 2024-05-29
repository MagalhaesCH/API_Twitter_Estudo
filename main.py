import pandas as pd

def save_tweets_to_csv(tweets, filename):
    df = pd.DataFrame(tweets["statuses"])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    query = "#example"
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    tweets = search_tweets(query, bearer_token)
    save_tweets_to_csv(tweets, "tweets.csv")
