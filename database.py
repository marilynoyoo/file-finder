from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///tasks.db')  # Change the database URL as needed

def setup_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    setup_database()
