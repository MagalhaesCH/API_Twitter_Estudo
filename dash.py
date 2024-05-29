import dash
from dash import dcc, html
import plotly.express as px

app = dash.Dash(__name__)

def create_dashboard(df):
    fig = px.histogram(df, x='sentiment', title="Distribuição de Sentimento dos Tweets")

    app.layout = html.Div(children=[
        html.H1(children='Análise de Sentimento dos Tweets'),
        dcc.Graph(
            id='sentiment-distribution',
            figure=fig
        )
    ])

if __name__ == "__main__":
    df = clean_data("tweets.csv")
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    create_dashboard(df)
    app.run_server(debug=True)
