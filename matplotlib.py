import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(df):
    sns.histplot(df['sentiment'], kde=True)
    plt.title("Distribuição de Sentimento dos Tweets")
    plt.xlabel("Sentimento")
    plt.ylabel("Frequência")
    plt.show()

if __name__ == "__main__":
    df = clean_data("tweets.csv")
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    plot_sentiment_distribution(df)
