from sqlalchemy import create_engine
from models import Base
#from connect import *

engine = create_engine("sqlite:///db.sqlite")


if __name__ == "__main__":
    Base.metadata.create_all(engine)