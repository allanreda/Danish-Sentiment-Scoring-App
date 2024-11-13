# Danish Sentiment Scoring App

Try it out live at: https://danish-sentiment-app-407428159583.us-central1.run.app/
![image](https://github.com/user-attachments/assets/11d9b8af-a4a9-4d4a-a97a-bc1d4628f13e)


This app performs sentiment analysis on Danish text using the Sentida library. It contains three functionalities: analyze a single text, compare two texts, and plot sentiment scores for longer texts. The app is designed with a user-friendly interface powered by Streamlit.

## Table of Contents
- [About the App](#about-the-app)
- [Single Text Analysis](#single-text-analysis)
- [Comparison of Two Texts](#comparison-of-two-texts)
- [Sentiment Plot for Longer Text](#sentiment-plot-for-longer-text)
- [Technologies](#technologies)

## About the App
Danish Sentiment Scoring allows users to:
- Analyze sentiment on Danish texts.
- Sentiment scores range from -1 (negative) to 1 (positive).
- You can analyze a single text, compare two texts, or visualize sentiment trends over longer texts.

Use the sidebar to navigate between sections and choose the feature you would like to use.

## Single Text Analysis
In this section, you can input a single text to receive an overall sentiment score. The app calculates the average sentiment of the text using Sentida.

## Comparison of Two Texts
This feature allows you to input two texts and compare their sentiment scores side by side. A bar chart is generated to help visualize the sentiment comparison between the two texts.

## Sentiment Plot for Longer Text
For longer texts, the app splits the text into individual sentences and calculates the sentiment score for each one. The results are then plotted on a graph, allowing you to visualize how sentiment changes throughout the text.

## Technologies
- Python: Backend development.
- Streamlit: Web app and frontend development.
- Sentida: Danish sentiment scoring.
- Matplotlib: Data visualization.
- Google Cloud Run: Deployment platform for running the application in a scalable and containerized environment.
