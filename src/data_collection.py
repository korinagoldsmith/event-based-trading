import yfinance as yf
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_stock_data(ticker):
    try:
        data = yf.download(ticker, start="2021-1-1", end="2023-1-31")
        if data.empty:
            raise ValueError(f"No data found for {ticker}. The stock might be delisted.")
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    return data

def fetch_event_data(keyword):
    api_key = os.getenv("NEWSAPI_KEY")
    
    newsapi = NewsApiClient(api_key=api_key)
    articles = newsapi.get_everything(q=keyword, language='en')
    return articles