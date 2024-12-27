from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Ticker, StockPrice

# Create a session
engine = create_engine('duckdb:///InvestmentDB.db')
Session = sessionmaker(bind=engine)
session = Session()

# Query all tickers
print("Tickers:")
tickers = session.query(Ticker).all()
for ticker in tickers:
    print(f"ID: {ticker.id}, Symbol: {ticker.ticker}, Price: {ticker.price}, Dividend Yield: {ticker.dividend_yield}")

# Query all stock prices
print("\nStock Prices:")
stock_prices = session.query(StockPrice).all()
for stock_price in stock_prices:
    print(f"Date: {stock_price.date}, Ticker: {stock_price.ticker}, Open: {stock_price.open}, Close: {stock_price.close}, High: {stock_price.high}, Low: {stock_price.low}, Volume: {stock_price.volume}")

# Close the session
session.close()