import yfinance as yf
import csv
import numpy as np

f = open("nasdaq.txt", "r")
urls = f.readlines()

cols = ['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']

i = 0
total = len(urls)

for url in urls:
    data = yf.download(
        # Maybe we can create a string including all indexes
        tickers = url,
        period = "max",
        interval = "1d",
        auto_adjust = False,
        threads = True,
        proxy = None,
    )
    file_name="./nasdaq/" + url + ".csv"
    data = data[cols]
    data.to_csv(file_name, index = True)
    i += 1
    print(f'{i} of {total} downloaded')