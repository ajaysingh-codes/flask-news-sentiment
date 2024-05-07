Table of Contents
About The project
Features
Project Structure
Getting started
Technologies Used

Overview
SentimentSpectrum is a web application designed to help users quickly understand the emotional tone of daily headlines by analyzing news articles related to user-defined topics. It leverages Natural Language Processing (NLP) to assess the sentiment of news articles and classify them as positive, negative, or neutral. This project aims to provide a user-friendly platform for news sentiment analysis and categorization.

Features
Text Sentiment Analysis: Users can input any text, and the application will analyze its sentiment, providing feedback on whether the sentiment is positive, negative, or neutral.
Topic-Based News Analysis: Users can input a topic, and the application will fetch relevant news articles, analyze their sentiment, and present the results.
Visual Data Representation: Sentiment analysis results are displayed using interactive bar charts, making it easy to comprehend the overall sentiment of articles.
News Article Summary: Provides a summary of the top news articles related to the input topic, allowing users to quickly access key information.

Project Structure
app.py: The main backend file that handles server-side logic, including routing, request handling, and template rendering.
Templates:
base.html: The base template provides the structure for all pages, including headers, navigation, and JavaScript libraries.
sentiment.html: Extends the base template to present a form for inputting text for sentiment analysis.
index.html: The homepage template where users can enter a topic to analyze related news articles.
results.html: Displays the sentiment analysis results for news articles, including a bar chart and individual article summaries.
Static Files:
index.css: Custom stylesheet that enhances the appearance of the application.




Getting Started

Configuration
To use the NewsAPI service, you'll need to obtain an API key by signing up on the NewsAPI website. Once you have the key:
Create a config.py file.
Add the following line to config.py:
API_KEY = '<Your_NewsAPI_Key>'
Replace <Your_NewsAPI_Key> with your actual API key.

How to Run
Clone the Repository: Clone the repository to your local system using git clone <repository_url>.
Install Dependencies: Use a virtual environment and install the required packages:
pip install -r requirements.txt
Run the Application: Start the Flask application:
flask run
Access the Application: Open a web browser and navigate to http://localhost:5000 to interact with the application.

Technologies Used

Backend: Flask for the server-side application logic.
Frontend: HTML, Bootstrap for styling, and Chart.js for data visualization.
NLP: Python libraries for sentiment analysis.

