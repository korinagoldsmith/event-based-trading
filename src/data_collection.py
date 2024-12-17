import yfinance as yf
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_stock_data(ticker):
    data = yf.download(ticker, start="2020-01-01", end="2023-12-01")
    return data

def fetch_event_data(keyword):
    api_key = os.getenv("NEWSAPI_KEY")
    if not api_key:
        raise ValueError("API key not found. Make sure NEWSAPI_KEY is set in your .env file.")
    
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(q=keyword, language='en')
    return articles