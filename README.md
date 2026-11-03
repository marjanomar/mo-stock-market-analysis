# Stock Market Analysis Using Python

## Overview
This project is a Python-based stock market analysis tool that retrieves and processes daily stock market data using the Alpha Vantage API. It analyzes five major technology companies to track recent stock performance and calculate daily percentage changes.

## Stocks Analyzed
- NVIDIA (NVDA)
- Advanced Micro Devices (AMD)
- Microsoft (MSFT)
- Alphabet (GOOGL)
- Apple (AAPL)

## Tools & Technologies
- **Python:** Core programming language
- **Pandas:** Data processing and analysis
- **Alpha Vantage API:** Retrieving daily stock market data
- **Requests:** Making API requests and retrieving financial data

## Key Features
- Retrieves daily historical stock market data through an API.
- Processes and organizes closing prices using pandas DataFrames.
- Calculates daily percentage changes to examine stock performance.
- Summarizes the most recent seven available trading days.
- Displays the latest closing price and recent percentage changes for each stock.

## How It Works
The script connects to the Alpha Vantage API to retrieve daily stock data for each selected company. It then processes the response, organizes the closing prices by date, calculates daily percentage changes, and outputs a summary of recent trading activity.

## Running the Project
1. Install the required Python libraries:
   `pip install pandas requests`
2. Obtain an API key from Alpha Vantage.
3. Set your API key as an environment variable named `ALPHAVANTAGE_API_KEY`.
4. Run the Python script:
   `python daily_stock_summary_safe.py`

## Project Purpose
I developed this project to gain hands-on experience working with financial data, API integration, and Python-based data analysis. It allowed me to explore how programming can be used to retrieve, process, and interpret market data in a structured way.
