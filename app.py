# Required imports
from flask import Flask, render_template, request, redirect, url_for
from newsapi import NewsApiClient
from config import API_KEY
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import pandas as pd

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import string

# Download NLTK datasets
def download_nltk_datasets():
    datasets = ['punkt', 'stopwords', 'wordnet']
    for dataset in datasets:
        try:
            nltk.download(dataset)
        except Exception as err:
            print(f"Failed to download dataset {dataset}: {str(err)}")

download_nltk_datasets()

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# News API client instance
newsapi = NewsApiClient(api_key=API_KEY)

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for querying articles
@app.route('/query_articles', methods=['POST'])
def query_articles():
    user_topic = request.form['user_topic']
    try:
        res = newsapi.get_everything(q=user_topic, language='en', sort_by='relevancy')
    except Exception as err:
        return f"Failed to fetch articles: {str(err)}"

    if not res.get('articles'):
        return "No articles found for this topic."

    articles = res['articles']
    df = pd.DataFrame(articles)

    df['content'] = df['content'].fillna('No content')

    # Preprocess and analyze sentiment of each article's content
    df['processed_content'] = df['content'].apply(preprocess_text)
    df['sentiment'] = df['processed_content'].apply(get_sentiment)
    sentiments = df['sentiment'].to_list()
    for article, sentiment in zip(articles, df['sentiment']):
        article['sentiment'] = sentiment

    sentiment_counts = df['sentiment'].value_counts()
    labels = sentiment_counts.index.to_list()
    values = sentiment_counts.values.tolist()

    return render_template('results.html', user_topic=user_topic, sentiment=sentiments, labels=labels, values=values, articles=articles)

@app.route('/user_sentiment', methods=['GET', 'POST'])
def user_sentiment():
    userText = ''
    sentiment = ''
    if request.method == 'POST':
        userText = request.form['userText']
        sentiment = get_sentiment(userText)
        return render_template('sentiment.html', sentiment=sentiment, userText=userText)
    else:
        return render_template('sentiment.html')


stop_words = set(stopwords.words('english'))
# Preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'(http | https)://\S+', ' ', text)

    # Remove punctuations
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords and lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return ' '.join(tokens)

# Method to get sentiment of a text
def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    compound_score = sentiment['compound']
    if compound_score > 0.5:
        return 'positive'
    elif compound_score < -0.5:
        return 'negative'
    else:
        return 'neutral'

if __name__ == '__main__':
    app.run(debug=True)
