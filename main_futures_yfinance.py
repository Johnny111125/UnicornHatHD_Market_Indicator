import yfinance as yf
import time
import subprocess

while True:
    # Get the current stock market futures
    stock_ticker = 'AAPL'
    stock_info = yf.Ticker(stock_ticker).info
    current_futures = stock_info['regularMarketPrice']

    # Get the previous close
    previous_close = stock_info['regularMarketPreviousClose']

    # Compare the current futures to the previous close
    if current_futures > previous_close:
        subprocess.run(["python", "green_up_arrow.py"])
    else:
        subprocess.run(["python", "red_up_arrow.py"])

    # Sleep for 30 seconds before checking again
    time.sleep(30)
