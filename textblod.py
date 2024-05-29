from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

if __name__ == "__main__":
    df = clean_data("tweets.csv")
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    print(df.head())
