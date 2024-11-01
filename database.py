from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = 'sqlite:///tasks.db'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Create a session factory
Session = sessionmaker(bind=engine)

def setup_database():
    """Create all tables in the database based on the models."""
    Base.metadata.create_all(engine)

def teardown_database():
    """Drop all tables in the database."""
    Base.metadata.drop_all(engine)
