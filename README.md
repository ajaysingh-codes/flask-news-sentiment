# News Sentiment Analysis Tool

## About The project
**SentimentSpectrum** is a web application designed to help users quickly understand the emotional tone of daily headlines by analyzing news articles related to user-defined topics. It leverages Natural Language Processing (NLP) to assess the sentiment of news articles and classify them as positive, negative, or neutral. This project aims to provide a user-friendly platform for news sentiment analysis and categorization.

## Features
- Text Sentiment Analysis: Users can input any text, and the application will analyze its sentiment, providing feedback on whether the sentiment is positive, negative, or neutral.
- Topic-Based News Analysis: Users can input a topic, and the application will fetch relevant news articles, analyze their sentiment, and present the results.
- Visual Data Representation: Sentiment analysis results are displayed using interactive bar charts, making it easy to comprehend the overall sentiment of articles.

## Getting Started
### Configuration
To use the NewsAPI service, you'll need to obtain an API key by signing up on the NewsAPI website. Once you have the key:
- Create a config.py file in the root folder.
- Add the following line to config.py:
API_KEY = '<Your_NewsAPI_Key>'
Replace <Your_NewsAPI_Key> with your actual API key.

### How to Run
- Clone the Repository: Clone the repository to your local system using git clone <repository_url>.
- Install Dependencies: Use a virtual environment and install the required packages:
pip install -r requirements.txt
- Run the Application: Start the Flask application:
flask run
- Access the Application: Open a web browser and navigate to interact with the application.

## Technologies Used
- Flask web framework (Python)
- HTML5 for website structure, Bootstrap and CSS3 for styling
- Chartjs for data visualization
- Natural Language Toolkit (NLTK) for tokenization and lemmatization
