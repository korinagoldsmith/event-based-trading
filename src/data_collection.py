import yfinance as yf
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_stock_data(ticker):
    data = yf.download(ticker, start="2024-12-10", end="2024-12-17")
    return data

def fetch_event_data(keyword):
    api_key = os.getenv("NEWSAPI_KEY")
    
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(q=keyword, language='en')
    return articles