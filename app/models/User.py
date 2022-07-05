# self is equivalent to this, and __init__() is equivalent to constructor() in JS

from app.db import Base
from sqlalchemy import Column, Integer, String

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

# created a User class that inherits from the Base class. Remember that earlier, we created Base as part of the db package

# User class, we declare several properties that the parent Base class will use to make the table. 
# We use classes from the sqlalchemy module to define the table columns and their data types. EX: nullable=False, which will become a SQL NOT NULL.