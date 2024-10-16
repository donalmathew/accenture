import requests
import os
API_KEY = os.getenv("API_KEY")

def get_trending_news(field):
    url = f'https://newsapi.org/v2/everything?q={field}&apiKey={API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return [article['title'] for article in articles[:5]]
