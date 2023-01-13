import yfinance as yf
import subprocess

# Assume the ticker symbol of the stock is stored in this variable
ticker = "VOO"

# Get the current close and open values
info = yf.Ticker(ticker).info
close = info['regularMarketPreviousClose']
open = info['regularMarketOpen']

if open > close:
    subprocess.run(["python", "green_up_arrow.py"])
else:
    subprocess.run(["python", "red_down_arrow.py"])
