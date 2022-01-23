from sqlalchemy import create_engine
from models import Base, Lead
from dbconfig import DATABASE_URI
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

