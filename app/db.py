from sqlalchemy import *
from sqlalchemy.orm import *

DATABASE_URL = "sqlite:///app.db"
engine = create_engine(DATABASE_URL, echo=False, future=True)
Base = declarative_base()