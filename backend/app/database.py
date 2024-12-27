from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def configure_database():
    # Create a DuckDB engine
    engine = create_engine('duckdb:///InvestmentDB.db')

    # Create tables
    Base.metadata.create_all(engine)

    # Return session factory
    Session = sessionmaker(bind=engine)
    return Session

if __name__ == "__main__":
    # Configure the database and create tables
    session_factory = configure_database()
    session = session_factory()

    # Example: Adding data to the database
    from models import Ticker, StockPrice

    ticker = Ticker(symbol="AAPL", price=150.0, dividend_yield=0.005)
    stock_price = StockPrice(date="2023-12-27", ticker="AAPL", open=149.0, close=151.0, high=152.0, low=148.0, volume=1000000)

    session.add(ticker)
    session.add(stock_price)
    session.commit()

    print("Database configured and sample data added.")