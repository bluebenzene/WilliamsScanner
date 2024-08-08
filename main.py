import yfinance as yf
from stock_indicators import indicators
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.enums import EndType

# Fetch historical quotes for AAPL from Yahoo Finance
def get_historical_quotes(ticker):
    df = yf.download(ticker, start="2023-01-01", end="2024-08-08")
    quotes_list = [
        Quote(date, open, high, low, close, volume) 
        for date, open, high, low, close, volume 
        in zip(df.index, df['Open'], df['High'], df['Low'], df['Close'], df['Volume'])
    ]
    return quotes_list

# Get AAPL historical quotes
quotes = get_historical_quotes("AAPL")

# Calculate the Williams Fractal indicator with a window span of 5
results = indicators.get_fractal(quotes, 2, EndType.HIGH_LOW)

# Print results
for r in results:
    print(f"Date: {r.date.date()}, Fractal Bear: {r.fractal_bear}, Fractal Bull: {r.fractal_bull}")
