from dotenv import dotenv_values
from simple_salesforce import Salesforce
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import logutils
from models import Lead
from crud import recreate_database, Session

config = dotenv_values(".env")

log = logutils.get_logger(__name__)

recreate_database()

log.info('Salesforce Username: ' + config["USERNAME"])
sf = Salesforce(username=config["USERNAME"], password=config["PASSWORD"], security_token=config["TOKEN"])
log.info('Successfully logged into Salesforce')

data = sf.query('SELECT Id, FirstName, LastName, Phone, Email FROM Lead')
log.info('Found %s Leads', data["totalSize"])

s = Session()

for lead in data["records"]:
    lead = Lead(
        id=lead['Id'],
        firstName=lead['FirstName'],
        lastName=lead['LastName'],
        email=lead['Email'],
        phone=lead['Phone']
    )

    s.add(lead)
    
s.commit()

leads = s.query(Lead).all()

for l in leads:
    log.info(l)

s.close()

# for rec in data["records"]:
#    log.info(rec["Name"])