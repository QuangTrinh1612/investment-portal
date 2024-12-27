from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.models import Base
from backend.app.core.config import settings

# Create a DuckDB engine
engine = create_engine(str(settings.sqlalchemy_database_uri))

def configure_database():
    # Create tables
    Base.metadata.create_all(engine)

    # Return session factory
    Session = sessionmaker(bind=engine)
    return Session