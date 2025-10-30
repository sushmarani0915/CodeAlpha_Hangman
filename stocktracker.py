import yfinance as yf

print("Welcome to Stock Tracker!")
stock_symbol = input("Enter stock symbol (like AAPL, TSLA, INFY.NS): ")

data = yf.Ticker(stock_symbol)
info = data.history(period="1d")

if info.empty:
    print("No data found. Please check the symbol and try again.")
else:
    price = info['Close'][0]
    print(f"Current price of {stock_symbol} is ₹{round(price, 2)}")
