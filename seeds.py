from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# where the db variables that you created earlier come into play. The code uses the Base class together with the engine connection variable to do two things. 
# First, it drops all the existing tables. 
# Second, it creates any tables that Base mapped, in a class that inherits Base (like User).