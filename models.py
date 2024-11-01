from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

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
    name = Column(String)
    email = Column(String)
    tasks = relationship("Task", order_by="Task.id", back_populates="user")
    categories = relationship("Category", order_by="Category.id", back_populates="user")

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="tasks")

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="categories")

if __name__ == "__main__":
    setup()  # Set up the database when the script is run
    print("Database setup complete.")
