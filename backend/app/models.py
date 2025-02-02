from sqlalchemy import Column, Integer, String, Float, Date, Sequence, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Initialize the Base class for declarative class definitions
Base = declarative_base()

# Define the Stock_Price table
class StockPrice(Base):
    __tablename__ = 'stock_price'

    date = Column(Date, primary_key=True)
    ticker = Column(String, ForeignKey('ticker.ticker'), primary_key=True)
    open = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)

    ticker_relationship = relationship("Ticker", back_populates="stock_prices")

# Define the Ticker table
class Ticker(Base):
    __tablename__ = 'ticker'

    stock_id_sequence = Sequence('stock_id_seq', start=1, increment=1)

    id = Column(Integer, stock_id_sequence, primary_key=True, server_default=stock_id_sequence.next_value())
    ticker = Column(String, unique=True, nullable=False)
    sector = Column(String)
    industry = Column(String)
    price = Column(Float)
    forward_pe = Column(Float)
    forward_eps = Column(Float)
    dividend_yield = Column(Float)
    ma50 = Column(Float)
    ma200 = Column(Float)

    stock_prices = relationship("StockPrice", back_populates="ticker_relationship")