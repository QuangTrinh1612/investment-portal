from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.models import Ticker, StockPrice, Base

def configure_database():
    # Create a DuckDB engine
    engine = create_engine('duckdb:///InvestmentDB.db')

    # Create tables
    Base.metadata.create_all(engine)

    # Return session factory
    Session = sessionmaker(bind=engine)
    return Session