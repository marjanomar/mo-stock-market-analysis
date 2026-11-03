import requests
import pandas as pd
import time
import os

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
STOCK_SYMBOLS = ['NVDA', 'AMD', 'MSFT', 'GOOGL', 'AAPL' ]  # Example symbols

if not API_KEY:
    raise RuntimeError("Set the ALPHAVANTAGE_API_KEY environment variable before running this script.")

def fetch_stock_data(symbol, api_key):
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(f"Response for {symbol}: {data}")  # Print the entire response to debug
    if "Time Series (Daily)" in data:
        return data
    else:
        print("No data available or invalid API response.")
        return None

def process_data(data):
    if data and 'Time Series (Daily)' in data:
        time_series = data['Time Series (Daily)']
        df = pd.DataFrame(time_series).T
        df = df[['4. close']]  # Only keep the closing price
        df.columns = ['Close Price']
        df.index.name = 'Date'
        df.index = pd.to_datetime(df.index)  # Convert index to datetime
        df = df.sort_index()  # Ensure data is sorted by date

        # Convert the 'Close Price' column to numeric (float)
        df['Close Price'] = pd.to_numeric(df['Close Price'], errors='coerce')

        # Calculate daily percentage change
        df['Daily Change (%)'] = df['Close Price'].pct_change() * 100

        return df
    return pd.DataFrame()


def analyze_stock(symbol):
    print(f"Fetching data for {symbol}...")
    data = fetch_stock_data(symbol, API_KEY)
    df = process_data(data)

    if not df.empty:
        # Filter only the last 7 rows (most recent trading days)
        recent_df = df.tail(7)  # Tail gives you the last 7 available entries
        latest_date = recent_df.index[-1]
        latest_close_price = recent_df.iloc[-1]['Close Price']
        print(f"Latest closing price for {symbol} on {latest_date}: ${latest_close_price}")

        # Print daily percentage change for the last 7 days
        print(f"Daily Percentage Change for {symbol} (Last 7 Days):")
        print(recent_df[['Daily Change (%)']])
    else:
        print(f"No data available for {symbol}")

def main():
    for symbol in STOCK_SYMBOLS:
        analyze_stock(symbol)
        time.sleep(15)  # Delay to avoid hitting the rate limit

if __name__ == '__main__':
    main()

