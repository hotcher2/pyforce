from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Lead(Base):
    __tablename__ = 'Lead'
    id = Column(String, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    # birthDate = Column(Date)
    email = Column(String)
    phone = Column(String)

    def __repr__(self):
        return "<Lead(id='{}', firstName='{}', lastName='{}', email='{}', phone='{}')>"\
                .format(self.id, self.firstName, self.lastName, self.email, self.phone)