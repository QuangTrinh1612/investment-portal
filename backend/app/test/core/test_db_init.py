from backend.app.core.database import configure_database
from backend.app.models import Ticker, StockPrice

# Configure the database and create tables
session_factory = configure_database()
session = session_factory()

ticker = Ticker(ticker="AAPL", price=150.0, dividend_yield=0.005)
stock_price = StockPrice(date="2023-12-27", ticker="AAPL", open=149.0, close=151.0, high=152.0, low=148.0, volume=1000000)

session.add(ticker)
session.add(stock_price)
session.commit()

print("Database configured and sample data added.")