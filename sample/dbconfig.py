### config.py ###

from dotenv import dotenv_values

config = dotenv_values(".env-sample")
dbusername = config['DBUSERNAME']
dbpassword = config['DBPASSWORD']
dbhost = config['DBHOST']
dbname = config['DBNAME']
dbport = config['DBPORT']

# Scheme: "postgresql+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
DATABASE_URI = f'postgresql+psycopg2://{dbusername}:{dbpassword}@{dbhost}:{dbport}/{dbname}'