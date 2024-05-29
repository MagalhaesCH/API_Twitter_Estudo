import pandas as pd

def clean_data(filename):
    df = pd.read_csv(filename)
    df = df[['created_at', 'text', 'user', 'retweet_count', 'favorite_count']]
    df['user'] = df['user'].apply(lambda x: eval(x)['screen_name'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    return df

if __name__ == "__main__":
    df = clean_data("tweets.csv")
    print(df.head())
