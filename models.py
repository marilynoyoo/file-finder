from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

# Create the SQLAlchemy engine
engine = create_engine('sqlite:///tasks.db')
Base = declarative_base()

def setup_database():
    """Create all tables in the database based on the models."""
    Base.metadata.create_all(engine)

def teardown_database():
    """Drop all tables in the database."""
    Base.metadata.drop_all(engine)

def drop_and_create():
    """Drop all tables in the database and create them again."""
    teardown_database()
    setup_database()

def setup():
    """Set up the database."""
    setup_database()

def teardown():
    """Teardown the database."""
    teardown_database()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    tasks = relationship("Task", back_populates="user")
    categories = relationship("Category", back_populates="user")

class Task(Base):
   class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="tasks")

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="categories")
if __name__ == "__main__":
    setup()  # Set up the database when the script is run
    print("Database setup complete.")
